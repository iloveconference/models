"""Functions to evaluate splitation models."""

from typing import Any
from typing import Callable
from typing import Optional

import numpy as np
from nltk.metrics.segmentation import pk  # type: ignore
from nltk.metrics.segmentation import windowdiff
from numpy.typing import NDArray

from models.split_utils import clean_text


def get_split_boundaries(splits: list[int]) -> str:
    """Get the boundaries of the splits (end of each split)."""
    boundaries = [0] * len(splits)
    boundaries[len(splits) - 1] = 1  # last split is always a boundary
    for i in range(0, len(splits) - 1):
        if splits[i] != splits[i + 1]:
            boundaries[i] = 1
    return "".join(map(str, boundaries))


def eval_split_boundaries(true_splits: list[int], pred_splits: list[int]) -> tuple[float, float, int]:
    """Evaluate the predicted splits against the true splits."""
    true_boundaries = get_split_boundaries(true_splits)
    pred_boundaries = get_split_boundaries(pred_splits)

    # set k to half of the average reference split length
    k = int(round(len(true_boundaries) / (true_boundaries.count("1") * 2.0)))
    pk_diff = pk(true_boundaries, pred_boundaries, k=k)
    window_diff = windowdiff(true_boundaries, pred_boundaries, k=k)
    count_diff = abs(true_boundaries.count("1") - pred_boundaries.count("1"))
    return pk_diff, window_diff, count_diff


def evaluate(
    talk_sections: list[dict[str, Any]],
    predictor: Callable[[list[str]], list[int]],
    debug: bool = False,
) -> dict[str, list[list[int]] | dict[str, float | int]]:
    """Predict splits for each talk_section and evaluate the results."""
    paras_total = 0
    pk_diff_total = 0.0
    window_diff_total = 0.0
    count_diff_total = 0
    count = 0
    all_pred_splits = []
    for talk_section in talk_sections:
        paragraphs = [clean_text(paragraph_split["text"]) for paragraph_split in talk_section["paragraphs"]]
        true_splits = [paragraph_split["split"] for paragraph_split in talk_section["paragraphs"]]
        paras_total += len(paragraphs)
        if debug:
            print(true_splits)
        # predict
        pred_splits = predictor(paragraphs)
        all_pred_splits.append(pred_splits)
        if debug:
            print(pred_splits)
        # eval - lower is better
        pk_diff, window_diff, count_diff = eval_split_boundaries(true_splits, pred_splits)
        if debug:
            print(pk_diff, window_diff, count_diff)
        pk_diff_total += pk_diff
        window_diff_total += window_diff
        count_diff_total += count_diff
        count += 1
    return {
        "predictions": all_pred_splits,
        "metrics": {
            "total": paras_total,
            "pk_diff": pk_diff_total / count,
            "window_diff": window_diff_total / count,
            "count_diff": count_diff_total / count,
        },
    }


def compare(
    talk_sections: list[dict[str, Any]],
    all_pred_splits: list[list[int]],
    ix: int,
    output: bool = True,
) -> int:
    """Compare the true and predicted splits for talk section at ix."""
    paragraphs = [clean_text(paragraph_split["text"]) for paragraph_split in talk_sections[ix]["paragraphs"]]
    true_splits = [paragraph_split["split"] for paragraph_split in talk_sections[ix]["paragraphs"]]
    pred_splits = all_pred_splits[ix]
    prev_true_split: Optional[int] = None
    prev_pred_split: Optional[int] = None
    diff_count = 0
    for ix, (paragraph, true_split, pred_split) in enumerate(zip(paragraphs, true_splits, pred_splits, strict=True)):
        separators = []
        if prev_true_split is not None and prev_true_split != true_split:
            separators.append("TTT")
        if prev_pred_split is not None and prev_pred_split != pred_split:
            separators.append("PPP")
        prev_true_split = true_split
        prev_pred_split = pred_split
        if len(separators) == 1:
            diff_count += 1
        if output:
            if len(separators) > 0:
                print("\n" + " ".join(separators))
            print(f"\n{ix} {paragraph}")
    return diff_count


def evaluate_embedder(
    talk_sections: list[dict[str, Any]],
    all_syntactic_splits: list[list[int]],
    embedder: Callable[[list[str]], list[NDArray[np.float32]]],
) -> tuple[list[float], list[float]]:
    """Evaluate an embedder.

    Evaluate the ability of an embedder to distinguish paragraphs in
    different splits.
    """
    pos_similarities = []
    neg_similarities = []
    for talk_section, syntactic_splits in zip(talk_sections, all_syntactic_splits, strict=True):
        paragraphs = [clean_text(paragraph_split["text"]) for paragraph_split in talk_section["paragraphs"]]
        true_splits = [paragraph_split["split"] for paragraph_split in talk_section["paragraphs"]]
        embeds = embedder(paragraphs)
        prev_true_split: Optional[int] = None
        prev_syntactic_split: Optional[int] = None
        for ix, (true_split, syntactic_split) in enumerate(zip(true_splits, syntactic_splits, strict=True)):
            true_division = False
            syntactic_division = False
            if prev_true_split is not None and prev_true_split != true_split:
                true_division = True
            if prev_syntactic_split is not None and prev_syntactic_split != syntactic_split:
                syntactic_division = True
            similarity = float(np.dot(embeds[ix - 1], embeds[ix]))
            # print(ix, true_split, syntactic_split, true_division, syntactic_division, similarity)
            if syntactic_division:
                if true_division:
                    pos_similarities.append(similarity)
                else:
                    neg_similarities.append(similarity)
            prev_true_split = true_split
            prev_syntactic_split = syntactic_split
    return pos_similarities, neg_similarities
