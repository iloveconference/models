"""Functions to evaluate segmentation models."""

from typing import Any
from typing import Callable
from typing import Optional

import numpy as np
from nltk.metrics.segmentation import pk  # type: ignore
from nltk.metrics.segmentation import windowdiff
from numpy.typing import NDArray

from models.data_utils import clean_text


def get_segment_boundaries(segments: list[int]) -> str:
    """Get the boundaries of the segments (end of each segment)."""
    boundaries = [0] * len(segments)
    boundaries[len(segments) - 1] = 1  # last segment is always a boundary
    for i in range(0, len(segments) - 1):
        if segments[i] != segments[i + 1]:
            boundaries[i] = 1
    return "".join(map(str, boundaries))


def eval_segment_boundaries(true_segments: list[int], pred_segments: list[int]) -> tuple[float, float, int]:
    """Evaluate the predicted segments against the true segments."""
    true_boundaries = get_segment_boundaries(true_segments)
    pred_boundaries = get_segment_boundaries(pred_segments)

    # set k to half of the average reference segment length
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
    """Predict segments for each talk_section and evaluate the results."""
    paras_total = 0
    pk_diff_total = 0.0
    window_diff_total = 0.0
    count_diff_total = 0
    count = 0
    all_pred_segments = []
    for talk_section in talk_sections:
        paragraphs = [clean_text(paragraph_segment["text"]) for paragraph_segment in talk_section["paragraphs"]]
        true_segments = [paragraph_segment["segment"] for paragraph_segment in talk_section["paragraphs"]]
        paras_total += len(paragraphs)
        if debug:
            print(true_segments)
        # predict
        pred_segments = predictor(paragraphs)
        all_pred_segments.append(pred_segments)
        if debug:
            print(pred_segments)
        # eval - lower is better
        pk_diff, window_diff, count_diff = eval_segment_boundaries(true_segments, pred_segments)
        if debug:
            print(pk_diff, window_diff, count_diff)
        pk_diff_total += pk_diff
        window_diff_total += window_diff
        count_diff_total += count_diff
        count += 1
    return {
        "predictions": all_pred_segments,
        "metrics": {
            "total": paras_total,
            "pk_diff": pk_diff_total / count,
            "window_diff": window_diff_total / count,
            "count_diff": count_diff_total / count,
        },
    }


def compare(
    talk_sections: list[dict[str, Any]],
    all_pred_segments: list[list[int]],
    ix: int,
    output: bool = True,
) -> int:
    """Compare the true and predicted segments for talk section at ix."""
    paragraphs = [clean_text(paragraph_segment["text"]) for paragraph_segment in talk_sections[ix]["paragraphs"]]
    true_segments = [paragraph_segment["segment"] for paragraph_segment in talk_sections[ix]["paragraphs"]]
    pred_segments = all_pred_segments[ix]
    prev_true_segment: Optional[int] = None
    prev_pred_segment: Optional[int] = None
    diff_count = 0
    for ix, (paragraph, true_segment, pred_segment) in enumerate(
        zip(paragraphs, true_segments, pred_segments, strict=True)
    ):
        separators = []
        if prev_true_segment is not None and prev_true_segment != true_segment:
            separators.append("TTT")
        if prev_pred_segment is not None and prev_pred_segment != pred_segment:
            separators.append("PPP")
        prev_true_segment = true_segment
        prev_pred_segment = pred_segment
        if len(separators) == 1:
            diff_count += 1
        if output:
            if len(separators) > 0:
                print("\n" + " ".join(separators))
            print(f"\n{ix} {paragraph}")
    return diff_count


def evaluate_embedder(
    talk_sections: list[dict[str, Any]],
    all_pred_segments: list[list[int]],
    embedder: Callable[[list[str]], list[NDArray[np.float32]]],
) -> tuple[list[float], list[float]]:
    """Evaluate an embedder.

    Evaluate the ability of an embedder to distinguish paragraphs in
    different segments.
    """
    pos_similarities = []
    neg_similarities = []
    for talk_section, pred_segments in zip(talk_sections, all_pred_segments, strict=True):
        paragraphs = [clean_text(paragraph_segment["text"]) for paragraph_segment in talk_section["paragraphs"]]
        true_segments = [paragraph_segment["segment"] for paragraph_segment in talk_section["paragraphs"]]
        embeds = embedder(paragraphs)
        prev_true_segment: Optional[int] = None
        prev_pred_segment: Optional[int] = None
        for ix, (true_segment, pred_segment) in enumerate(zip(true_segments, pred_segments, strict=True)):
            true_split = False
            pred_split = False
            if prev_true_segment is not None and prev_true_segment != true_segment:
                true_split = True
            if prev_pred_segment is not None and prev_pred_segment != pred_segment:
                pred_split = True
            similarity = float(np.dot(embeds[ix - 1], embeds[ix]))
            if pred_split:
                if true_split:
                    pos_similarities.append(similarity)
                else:
                    neg_similarities.append(similarity)
            prev_true_segment = true_segment
            prev_pred_segment = pred_segment
    return pos_similarities, neg_similarities
