"""Test cases for the segment_eval module."""

from typing import cast

from models import segment_eval


def test_get_segment_boundaries() -> None:
    """It returns the boundaries of the segments."""
    tests = [
        ([0], "1"),
        ([0, 0], "01"),
        ([0, 1], "11"),
        ([0, 1, 1], "101"),
        ([0, 1, 1, 2], "1011"),
    ]
    for segments, boundaries in tests:
        result = segment_eval.get_segment_boundaries(segments)
        assert result == boundaries


def test_eval_segment_boundaries() -> None:
    """It evaluates how closely the predicted boundaries match the true boundaries."""
    tests = [
        {
            "true_segments": [0, 0, 0, 1],
            "pred_segments": [0, 0, 0, 1],
            "pk_diff": 0.0,
            "window_diff": 0.0,
        },
        {
            "true_segments": [0, 0, 1, 1],
            "pred_segments": [0, 0, 0, 1],
            "pk_diff": 0.5,
            "window_diff": 0.5,
        },
    ]
    for test in tests:
        pk_diff, window_diff = segment_eval.eval_segment_boundaries(
            cast(list[int], test["true_segments"]),
            cast(list[int], test["pred_segments"]),
        )
        assert pk_diff == test["pk_diff"]
        assert window_diff == test["window_diff"]
