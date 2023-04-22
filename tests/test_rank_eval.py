"""Test cases for the rank_eval module."""

from typing import Union

import numpy as np
import pytest

from models import rank_eval


@pytest.mark.parametrize(
    "true_results, pred_results, k, expected",
    [
        (
            [
                {"id": 1, "score": 1},
                {"id": 2, "score": 4},
                {"id": 3, "score": 3},
                {"id": 4, "score": 2},
            ],
            [
                {"id": 1, "score": 1},
                {"id": 2, "score": 4},
                {"id": 4, "score": 2},
                {"id": 5, "score": 3},
            ],
            10,
            0.90,
        ),
        (
            [
                {"id": 1, "score": 1},
                {"id": 2, "score": 4},
                {"id": 3, "score": 3},
                {"id": 4, "score": 2},
            ],
            [
                {"id": 1, "score": 1},
                {"id": 2, "score": 4},
                {"id": 4, "score": 2},
                {"id": 5, "score": 3},
            ],
            3,
            0.725,
        ),
    ],
)
def test_get_ndcg(
    true_results: list[dict[str, Union[str, float]]],
    pred_results: list[dict[str, Union[str, float]]],
    k: int,
    expected: float,
) -> None:
    """It returns the NDCG score for two {id, score} lists."""
    result = rank_eval.get_ndcg(true_results, pred_results, k)
    assert np.isclose(result, expected, rtol=1e-2)
