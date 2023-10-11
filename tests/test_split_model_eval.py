"""Test cases for the split_model_eval module."""

from typing import cast

import numpy as np
from numpy.typing import NDArray

from models import split_model_eval


def test_get_split_boundaries() -> None:
    """It returns the boundaries of the splits."""
    tests = [
        ([0], "1"),
        ([0, 0], "01"),
        ([0, 1], "11"),
        ([0, 1, 1], "101"),
        ([0, 1, 1, 2], "1011"),
    ]
    for splits, boundaries in tests:
        result = split_model_eval.get_split_boundaries(splits)
        assert result == boundaries


def test_eval_split_boundaries() -> None:
    """It evaluates how closely the predicted boundaries match the true boundaries."""
    tests = [
        {
            "true_splits": [0, 0, 0, 1],
            "pred_splits": [0, 0, 0, 1],
            "pk_diff": 0.0,
            "window_diff": 0.0,
            "count_diff": 0,
        },
        {
            "true_splits": [0, 0, 1, 2],
            "pred_splits": [0, 0, 0, 1],
            "pk_diff": 0.25,
            "window_diff": 0.25,
            "count_diff": 1,
        },
    ]
    for test in tests:
        pk_diff, window_diff, count_diff = split_model_eval.eval_split_boundaries(
            cast(list[int], test["true_splits"]),
            cast(list[int], test["pred_splits"]),
        )
        assert pk_diff == test["pk_diff"]
        assert window_diff == test["window_diff"]
        assert count_diff == test["count_diff"]


def test_evaluate() -> None:
    """It evaluates the predicted splits for each talk section."""

    def dummy_predictor(paragraphs: list[str]) -> list[int]:
        return [1, 2, 3, 3]

    talk_sections = [
        {
            "paragraphs": [
                {"text": "Hello, world! ", "split": 1},
                {"text": "This is a test. ", "split": 2},
                {"text": "Another paragraph. ", "split": 2},
                {"text": "Yet another one. ", "split": 3},
            ]
        }
    ]

    expected_output = {
        "predictions": [[1, 2, 3, 3]],
        "metrics": {
            "total": 4,
            "pk_diff": 0.5,
            "window_diff": 0.5,
            "count_diff": 0,
        },
    }

    result = split_model_eval.evaluate(talk_sections, dummy_predictor, debug=False)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"


def test_compare() -> None:
    """It compares the true and predicted splits for a talk section."""
    talk_sections = [
        {
            "paragraphs": [
                {"text": "Hello, world! ", "split": 1},
                {"text": "This is a test. ", "split": 2},
                {"text": "Another paragraph. ", "split": 2},
                {"text": "Yet another one. ", "split": 3},
            ]
        }
    ]
    all_pred_splits = [[1, 2, 3, 3]]
    expected_differences = 2

    differences = split_model_eval.compare(talk_sections, all_pred_splits, 0, output=False)
    assert differences == expected_differences


def test_evaluate_embedder() -> None:
    """It evaluates an embedder."""

    def mock_embedder(paragraphs: list[str]) -> list[NDArray[np.float32]]:
        return [np.array([ix, ix]) for ix in range(len(paragraphs))]

    talk_sections = [
        {
            "paragraphs": [
                {"text": "This is a paragraph in split 1.", "split": 1},
                {"text": "This is another paragraph in split 1.", "split": 1},
                {"text": "This is a paragraph in split 2.", "split": 2},
                {"text": "This is another paragraph in split 2.", "split": 2},
            ]
        }
    ]

    all_pred_splits = [[1, 1, 2, 3]]

    # predicted transition from para 1 to para 2 is positive (true split changed)
    expected_pos_similarities = [4.0]
    # predicted transition from para 2 to 3 is negative (true split did not change)
    expected_neg_similarities = [12.0]

    pos_similarities, neg_similarities = split_model_eval.evaluate_embedder(
        talk_sections, all_pred_splits, mock_embedder
    )

    assert pos_similarities == expected_pos_similarities
    assert neg_similarities == expected_neg_similarities
