"""Utilities for splitting text into paragraphs and sections."""
import os
import re
from typing import Any
from typing import Callable
from typing import Generator
from typing import NamedTuple
from typing import Optional
from typing import cast

import numpy as np
from numpy.typing import NDArray
from voyageai import get_embeddings as get_voyageai_embeddings  # type: ignore


def get_mpnet_embedder(
    mpnet: Any,
    batch_size: int = 8,
) -> Callable[[list[str]], list[NDArray[np.float32]]]:
    """Get mpnet embeddings for paragraphs."""

    def embed(paragraphs: list[str]) -> list[NDArray[np.float32]]:
        embeds = []
        for ix in range(0, len(paragraphs), batch_size):
            ix_end = min(ix + batch_size, len(paragraphs))
            embeds.extend(mpnet.encode(paragraphs[ix:ix_end]))
        return cast(list[NDArray[np.float32]], embeds)

    return embed


def get_openai_embedder(
    openai: Any, engine: str = "text-embedding-ada-002"
) -> Callable[[list[str]], list[NDArray[np.float32]]]:
    """Get openai embeddings for paragraphs."""

    def embed(paragraphs: list[str]) -> list[NDArray[np.float32]]:
        res = openai.Embedding.create(input=paragraphs, engine=engine)
        return cast(list[NDArray[np.float32]], [record["embedding"] for record in res["data"]])

    return embed


def get_cohere_embedder(
    cohere: Any,
) -> Callable[[list[str]], list[NDArray[np.float32]]]:
    """Get cohere embeddings for paragraphs."""

    def embed(paragraphs: list[str]) -> list[NDArray[np.float32]]:
        # TODO if we end up using cohere, cache embeddings because they're so expensive
        res = cohere.embed(texts=paragraphs, model="large", truncate="END")
        return cast(list[NDArray[np.float32]], res.embeddings)

    return embed


def get_voyageai_embedder() -> Callable[[list[str]], list[NDArray[np.float32]]]:
    """Get voyageai embeddings for paragraphs."""

    def embed(paragraphs: list[str]) -> list[NDArray[np.float32]]:
        """Get Voyage AI embeddings for paragraphs."""
        embeds = []
        # batch size is 8
        for ix in range(0, len(paragraphs), 8):
            ix_end = min(ix + 8, len(paragraphs))
            embeds.extend(get_voyageai_embeddings(paragraphs[ix:ix_end], model="voyage-01", input_type="document"))
        return embeds

    return embed


def get_filenames(directory: str) -> list[str]:
    """Get filenames in directory."""
    return [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]


def get_sections(text: str) -> Generator[tuple[str, str], None, None]:
    """Get sections in text as (section title, section text)."""
    section_title = ""
    for ix, region in enumerate(re.split(r"([^\n]+)\n-{4,}(?:\n|$)", text)):
        if ix % 2 == 1:
            section_title = region.strip()
        elif len(region.strip()) > 0:
            yield section_title, region.strip()


def clean_text(text: str, keep_anchors: bool = False, keep_newlines: bool = False) -> str:
    """Clean text: remove headers, images, links, anchors, and extra whitespace."""
    # remove horizontal lines
    text = re.sub(r"[^\n]+\n-{4,}(\n|$)", "", text)
    # remove images
    text = re.sub(r"!\[([^\]]*)\]\([^\)]*\)(\s+Image[^\n]+)?", "", text)
    # remove links
    text = re.sub(r"\[([^\]]*)\]\([^\)]+\)", r"\1", text)
    # remove anchors
    if not keep_anchors:
        text = re.sub(r"<a name=\"[^\"]+\"></a>", "", text)
    # remove citations
    text = re.sub(r"\[[0-9]+\]", "", text)
    # convert fancy quotes to quotes
    text = re.sub(r"[‘’]", "'", text)
    text = re.sub(r"[“”]", '"', text)
    # convert nbsp and zero-width space to space
    text = text.replace("\u00a0", " ").replace("\u200b", " ")
    # remove carriage returns and tabs
    text = text.replace("\r", "").replace("\t", " ")
    # remove newlines and tabs
    if not keep_newlines:
        text = text.replace("\n", " ")
    # remove extra whitespace
    text = re.sub(r" +", " ", text)
    # strip
    text = text.lstrip()
    if not keep_newlines:
        text = text.rstrip()
    else:
        text = re.sub(r"(\s*\n){2,}", "\n\n", text)
    return text


def get_paragraph_id(paragraph: str) -> str:
    """Get paragraph ID."""
    match = re.search(r'<a name="(.*?)"', paragraph)
    if match:
        anchor_name = match.group(1)
        return anchor_name
    return ""


def get_paragraph_sentence_texts_and_ids(  # noqa: C901
    content: str, parser: Any, max_chars: int
) -> list[tuple[str, str]]:
    """Get paragraphs, lines, or sentences (text, anchor) from contents."""
    split_points = ["\n\n", "\n", "SENTENCE", ""]
    texts = [clean_text(content, keep_anchors=True, keep_newlines=True)]
    for split_point in split_points:
        if split_point == "SENTENCE" and parser is None:
            continue
        splits = []
        too_long = False
        for text in texts:
            if len(text) > max_chars:
                too_long = True
                # split at split point
                if split_point == "SENTENCE":
                    ts = [sent.text for sent in parser(text).sents]
                elif split_point == "":
                    ts = []
                    for ix in range(0, len(text), max_chars):
                        ts.append(text[ix : ix + max_chars])
                else:
                    ts = text.split(split_point)
                # extra is the split point unless we split on sentences
                extra = split_point if split_point != "SENTENCE" else " "
                for t in ts:
                    splits.append(t + extra)
            else:
                splits.append(text)
        if not too_long:
            break
        texts = splits

    # add paragraph IDs
    paragraph_texts_and_ids = []
    curr_id = ""
    prev_text = ""
    for text in texts:
        if text.strip() == "":
            prev_text += text
            continue
        if prev_text:
            paragraph_texts_and_ids.append((clean_text(prev_text, keep_newlines=True), curr_id))
        prev_text = text
        _id = get_paragraph_id(text)
        if _id:
            curr_id = _id
    if prev_text:
        paragraph_texts_and_ids.append((clean_text(prev_text, keep_newlines=True), curr_id))
    return paragraph_texts_and_ids


def split_on_markdown_headers(content: str, max_chars: int) -> list[tuple[str, list[str]]]:
    """Split text on markdown headers."""
    split_points = [
        (r"(?:^|\n)(?:# ([^\n]+)\n)", "\n"),
        (r"(?:^|\n)(?:## ([^\n]+)\n)", "\n"),
        (r"(?:^|\n)(?:### ([^\n]+)\n)", "\n"),
        (r"(?:^|\n)(?:#### ([^\n]+)\n)", "\n"),
        (r"(?:^|\n)(?:\*{3,})(\n)", "\n"),
        (r"(?:^|\n)(?:-{3,})(\n)", "\n"),
        (r"(?:^|\n)(?:_{3,})(\n)", "\n"),
        (r"(?:^|\n\n)(?:\*\*([^\n]+)\*\*\s*\n\s*\n)", "\n\n"),
    ]  # noqa: W605
    text_headers: list[tuple[str, list[str]]] = [(clean_text(content, keep_anchors=True, keep_newlines=True), [])]
    for split_point, extra in split_points:
        split_headers = []
        too_long = False
        for text, headers in text_headers:
            if len(text) > max_chars:
                too_long = True
                # split at split point
                parts = re.split(split_point, text)
                if len(parts[0].strip()) > 0:
                    split_headers.append((parts[0].lstrip() + (extra if len(parts) > 1 else ""), headers))
                for ix in range(1, len(parts), 2):
                    part = parts[ix + 1]
                    if ix < len(parts) - 2:
                        part += extra
                    header = parts[ix].strip()
                    new_headers = headers + [header] if len(header) > 0 else headers
                    split_headers.append((part.lstrip(), new_headers))
            else:
                split_headers.append((text, headers))
        if not too_long:
            break
        text_headers = split_headers
    return text_headers


def get_paragraph_texts_and_ids(contents: str) -> list[tuple[str, str]]:
    """Get paragraphs (text, anchor) from contents."""
    paragraphs = []
    for paragraph in contents.split("\n\n"):
        _id = get_paragraph_id(paragraph)
        paragraph = clean_text(paragraph).strip()
        if not paragraph:
            continue
        paragraphs.append((paragraph + "\n\n", _id))
    return paragraphs


def _count_words(texts: list[str]) -> int:
    """Count words in texts."""
    return sum(len(text.split()) for text in texts)


def get_split_texts_and_ids(
    paragraph_texts_and_ids: list[tuple[str, str]], split_ixs: list[int], max_split_len: Optional[int] = None
) -> list[tuple[str, str]]:
    """Group paragraphs into splits, and use the earliest anchor as the split ID."""
    splits = []
    curr_split_id = ""
    curr_split_ix = 0
    curr_split: list[str] = []
    for (paragraph, _id), split_ix in zip(paragraph_texts_and_ids, split_ixs, strict=True):
        if split_ix != curr_split_ix or (
            max_split_len is not None and _count_words(curr_split) + _count_words([paragraph]) > max_split_len
        ):
            if len(curr_split) > 0:
                splits.append(("".join(curr_split).strip(), curr_split_id))
            if split_ix == curr_split_ix:
                curr_split = [curr_split[-1]]  # overlap
            else:
                curr_split = []
            curr_split_id = ""
            curr_split_ix = split_ix
        if curr_split_id == "" and _id != "":
            curr_split_id = _id
        curr_split.append(paragraph)
    if len(curr_split) > 0:
        splits.append(("".join(curr_split).strip(), curr_split_id))
    return splits


class Annotation(NamedTuple):
    """Annotation."""

    start: int
    end: int
    label: str


def get_annotations(annotations_in: list[dict[str, Any]]) -> list[Annotation]:
    """Get annotations from annotations_in."""
    # gather all results
    results = []
    for annotation in annotations_in:
        for result in annotation["result"]:
            if len(result["value"]["labels"]) != 1:
                raise ValueError("should be one label", len(result["value"]["labels"]))
            results.append(result)
    # create annotations from sorted results
    annotations = []
    start: Optional[int] = None
    label: Optional[str] = None
    end: Optional[int] = None
    for result in sorted(results, key=lambda res: res["value"]["start"]):
        if label != result["value"]["labels"][0]:
            if label is not None:
                # save previous split
                assert start is not None
                assert end is not None
                annotations.append(Annotation(start, end, label))
            start = result["value"]["start"]
            label = result["value"]["labels"][0]
        end = result["value"]["end"]
    if label is not None:
        # save final split
        assert start is not None
        assert end is not None
        annotations.append(Annotation(start, end, label))
    return annotations


def get_label_for_paragraph(start: int, end: int, annotations: list[Annotation]) -> str:
    """Get label for paragraph."""
    for annotation in annotations:
        # fuzzy match in case boundaries are off by a bit
        if start >= annotation.start - 3 and end <= annotation.end + 3:
            return annotation.label
    raise ValueError("annotation not found", start, end, annotations)


def get_paragraph_splits(annotations: list[Annotation], text: str) -> list[dict[str, Any]]:
    """Split text into paragraphs, and assign a split ID to each paragraph."""
    paragraph_splits = []
    start = 0
    split = 0
    prev_label = None
    for ix, paragraph in enumerate(re.split(r"(\n{2,})", text)):
        if ix % 2 == 1:
            start += len(paragraph)
            continue
        end = start + len(paragraph)
        label = get_label_for_paragraph(start, end, annotations)
        if label != prev_label:
            prev_label = label
            split += 1
        paragraph_splits.append(
            {
                "text": paragraph.strip(),
                "split": split,
            }
        )
        start = end
    return paragraph_splits
