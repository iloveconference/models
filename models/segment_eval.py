"""Functions to evaluate segmentation models."""

from nltk.metrics.segmentation import pk  # type: ignore
from nltk.metrics.segmentation import windowdiff


def get_segment_boundaries(segments: list[int]) -> str:
    """Get the boundaries of the segments (end of each segment)."""
    boundaries = [0] * len(segments)
    boundaries[len(segments) - 1] = 1  # last segment is always a boundary
    for i in range(0, len(segments) - 1):
        if segments[i] != segments[i + 1]:
            boundaries[i] = 1
    return "".join(map(str, boundaries))


def eval_segment_boundaries(
    true_segments: list[int], pred_segments: list[int]
) -> tuple[float, float]:
    """Evaluate the predicted segments against the true segments."""
    true_boundaries = get_segment_boundaries(true_segments)
    pred_boundaries = get_segment_boundaries(pred_segments)

    # set k to half of the average reference segment length
    k = int(round(len(true_boundaries) / (true_boundaries.count("1") * 2.0)))
    pk_diff = pk(true_boundaries, pred_boundaries, k=k)
    window_diff = windowdiff(true_boundaries, pred_boundaries, k=k)
    return pk_diff, window_diff
