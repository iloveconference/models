"""Functions to train splitation models."""
import re
from typing import Any
from typing import Callable
from typing import Optional
from typing import cast

import numpy as np
import pandas as pd  # type: ignore
from numpy.typing import NDArray
from tqdm import tqdm

from models.split_utils import clean_text


def get_bert_wiki_paras_scorer(pipe: Any) -> Callable[[str, str], float]:
    """Score paragraph pairs using bert-wiki-paragraphs."""

    def score(para1: str, para2: str) -> float:
        para_pair = f"{para1} [SEP] {para2}"
        result = pipe(para_pair, truncation=True)[0]
        return cast(float, result["score"])

    return score


def predict_using_pairs(pair_scorer: Callable[[str, str], float], threshold: float) -> Callable[[list[str]], list[int]]:
    """Predict splits using pair scores."""

    def predict(paragraphs: list[str]) -> list[int]:
        current = 1
        splits = [current]
        for i in range(1, len(paragraphs)):
            score = pair_scorer(paragraphs[i - 1], paragraphs[i])
            if score < threshold:
                current += 1
            splits.append(current)
        return splits

    return predict


def predict_using_embeddings(
    embedder: Callable[[list[str]], list[NDArray[np.float32]]], threshold: float
) -> Callable[[list[str]], list[int]]:
    """Predict splits using embeddings."""

    def predict(paragraphs: list[str]) -> list[int]:
        embeddings = embedder(paragraphs)
        current = 1
        splits = [current]
        for i in range(1, len(embeddings)):
            score = np.dot(embeddings[i - 1], embeddings[i])
            if score < threshold:
                current += 1
            splits.append(current)
        return splits

    return predict


def syntactic_paragraph_features(text: str) -> dict[str, int]:
    """Get syntactic features for a paragraph."""
    quote_prefix = re.match(r'(.*?)(?:^|[:;,]\s+)"', text)
    return {
        # is a markdown header or bold text
        "is_header": 1 if re.match(r"\s*#{2,6}\s[^\n]+\s*$", text) or re.match(r"\s*\*{2}[^\n]+\*{2}\s*$", text) else 0,
        # begins with * or a number or a letter or roman numeral
        "is_list": 1 if re.match(r"\s*(?:\*|\(?[0-9]+[.)]?|\(?[A-Za-z][.)]|\(?[ivx]+[.)])\s", text) else 0,
        # ends in :
        "ends_with_colon": 1 if re.search(r":\s*$", text) else 0,
        # is <= 12 space-separated words
        "is_short": 1 if len(text.split(" ")) <= 12 else 0,
        # is a quote
        "is_quote": 1 if quote_prefix is not None and len(quote_prefix[1].strip().split(" ")) <= 4 else 0,
    }


def predict_using_syntactic_features(
    syntactic_feature_generator: Callable[[str], dict[str, int]]
) -> Callable[[list[str]], list[int]]:
    """Predict splits using syntactic features."""

    def predict(paragraphs: list[str]) -> list[int]:
        current = 1
        splits = []
        features: Optional[dict[str, int]] = None
        next_features: Optional[dict[str, int]] = (
            syntactic_feature_generator(paragraphs[0]) if len(paragraphs) > 0 else None
        )
        for i in range(len(paragraphs)):
            prev_features = features
            features = next_features
            next_features = syntactic_feature_generator(paragraphs[i + 1]) if i + 1 < len(paragraphs) else None
            if features is None:  # for the type checker so it doesn't complain about features being None
                pass
            elif (
                i == 0
                or features["is_list"]
                or features["is_quote"]
                or (prev_features is not None and prev_features["ends_with_colon"])
                or (
                    features["is_short"]
                    and not features["ends_with_colon"]
                    and (next_features is None or not next_features["is_quote"])
                )
                or (prev_features is not None and prev_features["is_header"] and prev_features["is_short"])
            ):
                pass
            else:
                current += 1
            splits.append(current)
        return splits

    return predict


def group_paragraphs_using_syntactic_features(
    syntactic_feature_generator: Callable[[str], dict[str, int]], paragraphs: list[str], max_chars: int = 2000
) -> list[list[str]]:
    """Group paragraphs using syntactic features."""
    syntactic_predictor = predict_using_syntactic_features(syntactic_feature_generator)
    feature_splits = syntactic_predictor(paragraphs)
    prev_split = None
    group_len = 0
    paragraph_groups = []
    group: list[str] = []
    for paragraph, feature_split in zip(paragraphs, feature_splits, strict=True):
        if len(group) > 0 and (feature_split != prev_split or group_len + len(paragraph) > max_chars):
            paragraph_groups.append(group)
            group = []
            group_len = 0
        group.append(paragraph)
        group_len += len(paragraph)
        prev_split = feature_split
    paragraph_groups.append(group)
    return paragraph_groups


def predict_using_features_and_embeddings(
    syntactic_feature_generator: Callable[[str], dict[str, int]],
    embedder: Callable[[list[str]], list[NDArray[np.float32]]],
    threshold: float,
) -> Callable[[list[str]], list[int]]:
    """Predict splits using syntactic features followed by embeddings."""

    def predict(paragraphs: list[str]) -> list[int]:
        # first group paragraphs using syntactic features
        paragraph_groups = group_paragraphs_using_syntactic_features(syntactic_feature_generator, paragraphs)
        # next get embeddings for paragraph groups
        embeddings = embedder(["\n".join(group) for group in paragraph_groups])
        # finally generate splits for each group based on embeddings
        current = 1
        splits = [current] * len(paragraph_groups[0])
        for ix in range(1, len(embeddings)):
            score = np.dot(embeddings[ix - 1], embeddings[ix])
            if score < threshold:
                current += 1
            splits.extend([current] * len(paragraph_groups[ix]))
        return splits

    return predict


def predict_using_features_and_greedy_embeddings(  # noqa: C901
    syntactic_feature_generator: Callable[[str], dict[str, int]],
    embedder: Callable[[list[str]], list[NDArray[np.float32]]],
    high_similarity_threshold: float = 0.83,
    max_chars: int = 2000,
    min_chars: int = 100,
    low_similarity_threshold: float = 0.5,
    low_max_split_length: int = 400,
    low_max_length_difference: int = 50,
) -> Callable[[list[str]], list[int]]:
    """Predict splits using syntactic features followed by embeddings."""

    def _paragraph_group_length(
        ix: int, paragraph_group_assignments: list[int], paragraph_group_texts: list[str]
    ) -> int:
        return sum(
            len(paragraph_group_texts[i])
            for i, assignment in enumerate(paragraph_group_assignments)
            if assignment == paragraph_group_assignments[ix]
        )

    def _merge_paragraph_groups(ix1: int, ix2: int, paragraph_group_assignments: list[int]) -> None:
        assignment1 = paragraph_group_assignments[ix1]
        assignment2 = paragraph_group_assignments[ix2]
        for ix, assignment in enumerate(paragraph_group_assignments):
            if assignment == assignment2:
                paragraph_group_assignments[ix] = assignment1

    def predict(paragraphs: list[str]) -> list[int]:
        # first group paragraphs using syntactic features
        paragraph_groups = group_paragraphs_using_syntactic_features(syntactic_feature_generator, paragraphs, max_chars)
        # next get embeddings for paragraph groups
        paragraph_group_texts = ["\n".join(group) for group in paragraph_groups]
        embeddings = embedder(paragraph_group_texts)
        # finally merge paragraph groups greedily based on embeddings as long as max_chars is not exceeded
        pair_scores = [np.dot(embeddings[ix], embeddings[ix + 1]) for ix in range(len(paragraph_groups) - 1)]
        paragraph_group_assignments = [ix for ix in range(len(paragraph_groups))]
        sorted_pair_scores = sorted(enumerate(pair_scores), key=lambda x: x[1], reverse=True)

        for ix, score in sorted_pair_scores:
            if score < low_similarity_threshold:
                break
            group_len = _paragraph_group_length(ix, paragraph_group_assignments, paragraph_group_texts)
            next_group_len = _paragraph_group_length(ix + 1, paragraph_group_assignments, paragraph_group_texts)

            if group_len + next_group_len > max_chars:
                continue

            # If a long paragraph is split into sentences, do we want min_chars to be lower
            # and low_max_length_difference to be higher so that individual sentences are more likely to get combined?
            if score >= high_similarity_threshold or (
                score >= low_similarity_threshold
                and min_chars <= group_len < low_max_split_length
                and min_chars <= next_group_len < low_max_split_length
                and abs(group_len - next_group_len) < low_max_length_difference
            ):
                # Merge
                _merge_paragraph_groups(ix, ix + 1, paragraph_group_assignments)

        # finally generate splits based on assignments
        current = 1
        splits = [current] * len(paragraph_groups[0])
        for ix in range(1, len(paragraph_groups)):
            if paragraph_group_assignments[ix] != paragraph_group_assignments[ix - 1]:
                current += 1
            splits.extend([current] * len(paragraph_groups[ix]))
        return splits

    return predict


def predict_using_features_and_ensemble(
    syntactic_feature_generator: Callable[[str], dict[str, int]],
    openai_embedder: Callable[[list[str]], list[NDArray[np.float32]]],
    mpnet_embedder: Callable[[list[str]], list[NDArray[np.float32]]],
    parser: Any,
    clf: Any,
    threshold: float,
) -> Callable[[list[str]], list[int]]:
    """Predict splits using syntactic features and an ensemble."""

    def predict(paragraphs: list[str]) -> list[int]:
        # first group paragraphs using syntactic features
        paragraph_groups = group_paragraphs_using_syntactic_features(syntactic_feature_generator, paragraphs)
        paragraph_group_texts = ["\n".join(group) for group in paragraph_groups]
        # next get embeddings for paragraph groups
        openai_embeds = openai_embedder(paragraph_group_texts)
        mpnet_embeds = mpnet_embedder(paragraph_group_texts)
        # finally generate splits for each group based on classifier
        current = 1
        splits = [current] * len(paragraph_groups[0])
        for ix in range(1, len(paragraph_groups)):
            features = get_pair_features(ix - 1, ix, openai_embeds, mpnet_embeds, parser, paragraph_group_texts)
            features_df = pd.DataFrame([features])
            score = clf.predict_proba(features_df)[0][1]
            if score < threshold:
                current += 1
            splits.extend([current] * len(paragraph_groups[ix]))
        return splits

    return predict


def count_words(tokens: list[Any]) -> int:
    """Count words in a list of spaCy tokens."""
    return len([token for token in tokens if token.pos_ != "PUNCT"])


def get_text_features(prefix: str, text: str, parser: Any) -> dict[str, float]:
    """Get features for a text."""
    doc = parser(text)
    tokens = list(doc)
    sentences = list(doc.sents)

    return {
        # number tokens (1/(len(tokens)+1))
        f"{prefix}_tokens": 1 / (count_words(tokens) + 1),
        # number sentences (1/(len(sentences)+1))
        f"{prefix}_sentences": 1 / (len(sentences) + 1),
    }


# get pair features
def get_pair_features(
    prev_ix: int,
    curr_ix: int,
    openai_embeds: list[NDArray[np.float32]],
    mpnet_embeds: list[NDArray[np.float32]],
    parser: Any,
    texts: list[str],
) -> dict[str, float]:
    """Get features for a pair of paragraphs."""
    features = {
        "openai": float(np.dot(openai_embeds[prev_ix], openai_embeds[curr_ix])),
        "mpnet": float(np.dot(mpnet_embeds[prev_ix], mpnet_embeds[curr_ix])),
        #         'bert_wiki': bert_wiki_paras_scorer(texts[prev], texts[curr]),
    }
    features.update(get_text_features("left", texts[prev_ix], parser))
    features.update(get_text_features("right", texts[curr_ix], parser))
    return features


def get_labeled_pairs(
    talk_sections: list[dict[str, Any]],
    openai_embedder: Callable[[list[str]], list[NDArray[np.float32]]],
    mpnet_embedder: Callable[[list[str]], list[NDArray[np.float32]]],
    parser: Any,
    syntactic_feature_generator: Callable[[str], dict[str, int]],
) -> list[dict[str, Any]]:
    """Get labeled pairs for training.

    Label is 1 if the two paragraphs are in the same split, 0 otherwise.
    """
    pairs = []
    for talk_section in tqdm(talk_sections):
        paragraphs = [clean_text(paragraph_split["text"]) for paragraph_split in talk_section["paragraphs"]]
        true_splits = [paragraph_split["split"] for paragraph_split in talk_section["paragraphs"]]
        # first group paragraphs using syntactic features
        paragraph_groups = group_paragraphs_using_syntactic_features(syntactic_feature_generator, paragraphs)
        paragraph_group_texts = ["\n".join(group) for group in paragraph_groups]
        # next get embeddings for paragraph groups
        openai_embeds = openai_embedder(paragraph_group_texts)
        mpnet_embeds = mpnet_embedder(paragraph_group_texts)
        prev_paragraphs = 0
        # finally, generate pairs
        for ix in range(1, len(paragraph_groups)):
            left_split = true_splits[prev_paragraphs]
            right_split = true_splits[prev_paragraphs + len(paragraph_groups[ix - 1])]
            prev_paragraphs += len(paragraph_groups[ix - 1])
            features = get_pair_features(ix - 1, ix, openai_embeds, mpnet_embeds, parser, paragraph_group_texts)
            features["label"] = 1 if left_split == right_split else 0
            pairs.append(features)
    return pairs


def get_paragraph_ngram_pairs(paragraph_splits: list[dict[str, Any]], ngram_size: int = 5) -> list[dict[str, Any]]:
    """Generate ngram pairs from paragraph splits.

    Label the pair with a 1 if the paragraphs belong to different splits,
    or a 0 if they belong to the same split.

    NOT USED
    """
    ngram_pairs = []
    for i_start in range(0, len(paragraph_splits)):
        for i_end in range(1, ngram_size + 1):
            if (
                i_start + i_end > len(paragraph_splits)
                or paragraph_splits[i_start]["split"] != paragraph_splits[i_start + i_end - 1]["split"]
            ):
                continue
            i_text = "\n\n".join(
                paragraph_split["text"] for paragraph_split in paragraph_splits[i_start : i_start + i_end]
            )
            j_start = i_start + i_end
            for j_end in range(1, ngram_size + 1):
                if (
                    j_start + j_end > len(paragraph_splits)
                    or paragraph_splits[j_start]["split"] != paragraph_splits[j_start + j_end - 1]["split"]
                ):
                    continue
                j_text = "\n\n".join(
                    paragraph_split["text"] for paragraph_split in paragraph_splits[j_start : j_start + j_end]
                )
                ngram_pairs.append(
                    {
                        "ngrams_left": i_end,
                        "ngrams_right": j_end,
                        "text_left": i_text,
                        "text_right": j_text,
                        "label": 1 if paragraph_splits[i_start]["split"] != paragraph_splits[j_start]["split"] else 0,
                    }
                )
    return ngram_pairs
