"""Functions to evaluate ranking models."""
from typing import Union
from typing import cast

import numpy as np
from sklearn.metrics import ndcg_score  # type: ignore


def get_ndcg(
    true_results: list[dict[str, Union[str, float]]], pred_results: list[dict[str, Union[str, float]]], k: int = 10
) -> float:
    """Return the Normalized Discounted Cumulative Gain score for two {id, score} lists."""
    all_results = list({result["id"] for result in true_results} | {result["id"] for result in pred_results})
    true_scores = [
        next((item["score"] for item in true_results if item["id"] == result), 0.0) for result in all_results
    ]
    pred_scores = [
        next((item["score"] for item in pred_results if item["id"] == result), 0.0) for result in all_results
    ]
    return cast(float, ndcg_score(np.asarray([true_scores]), np.asarray([pred_scores]), k=k))
