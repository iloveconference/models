"""Test cases for the split_model_train module."""

from typing import Iterator
from typing import NamedTuple

import numpy as np
import pandas as pd  # type: ignore
from numpy.typing import NDArray

from models import split_model_train


def test_predict_using_pairs() -> None:
    """It predicts the splits for each paragraph using the paragraph pairs."""

    def dummy_pair_scorer(text1: str, text2: str) -> float:
        if text1.endswith("world!") and text2.startswith("This"):
            return 0.2
        return 0.6

    threshold = 0.5
    predictor = split_model_train.predict_using_pairs(dummy_pair_scorer, threshold)

    paragraphs = [
        "Hello, world!",
        "This is a test.",
        "Another paragraph.",
        "Yet another one.",
    ]

    expected_output = [1, 2, 2, 2]

    result = predictor(paragraphs)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"


def test_predict_using_embeddings() -> None:
    """It predicts the splits for each paragraph using the paragraph embeddings."""

    def dummy_embedder(paragraphs: list[str]) -> list[NDArray[np.float32]]:
        embeddings = [
            np.array([0.5, 0.5], dtype=np.float32),
            np.array([0.7, 0.3], dtype=np.float32),
            np.array([0.6, 0.4], dtype=np.float32),
            np.array([0.4, 0.6], dtype=np.float32),
        ]
        return embeddings

    threshold = 0.5

    predictor = split_model_train.predict_using_embeddings(dummy_embedder, threshold)

    paragraphs = [
        "Hello, world!",
        "This is a test.",
        "Another paragraph.",
        "Yet another one.",
    ]

    expected_output = [1, 1, 1, 2]

    result = predictor(paragraphs)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"


def test_syntactic_paragraph_features() -> None:
    """It returns the syntactic features for a paragraph."""
    tests = [
        (
            "* Hello, world!",
            {"is_list": 1, "ends_with_colon": 0, "is_short": 1, "is_quote": 0},
        ),
        (
            "(1) This",
            {"is_list": 1, "ends_with_colon": 0, "is_short": 1, "is_quote": 0},
        ),
        (
            "10 And that",
            {"is_list": 1, "ends_with_colon": 0, "is_short": 1, "is_quote": 0},
        ),
        (
            "I. am that I AM",
            {"is_list": 1, "ends_with_colon": 0, "is_short": 1, "is_quote": 0},
        ),
        (
            "I am he who was",
            {"is_list": 0, "ends_with_colon": 0, "is_short": 1, "is_quote": 0},
        ),
        (
            "ends in colon:",
            {"is_list": 0, "ends_with_colon": 1, "is_short": 1, "is_quote": 0},
        ),
        (
            'and again, "I say unto you that Christ shall come into the world',
            {"is_list": 0, "ends_with_colon": 0, "is_short": 0, "is_quote": 1},
        ),
        (
            '"This is my body',
            {"is_list": 0, "ends_with_colon": 0, "is_short": 1, "is_quote": 1},
        ),
        (
            'Not a "Quote"',
            {"is_list": 0, "ends_with_colon": 0, "is_short": 1, "is_quote": 0},
        ),
        (
            'This is also not a: "Quote"',
            {"is_list": 0, "ends_with_colon": 0, "is_short": 1, "is_quote": 0},
        ),
    ]

    for paragraph, result in tests:
        features = split_model_train.syntactic_paragraph_features(paragraph)
        assert features == result, f"Expected {result}, but got {features}"


def test_predict_using_syntactic_features() -> None:
    """It predicts the splits for each paragraph using the syntactic features."""
    predictor = split_model_train.predict_using_syntactic_features(split_model_train.syntactic_paragraph_features)

    paragraphs = [
        "Hello, world! ",
        "this is a long sentence that should not be combined with the one above",
        "* List item that is long but it should be combined with the one above",
        "* Another list item that is long but it should be combined with the one above",
        "this is a long sentence that should not be combined with the one above",
        "Ends in a colon:",
        "this is a long sentence but it should be combined with the one ending in colon above",
        '"This is a quote that is long but it should be combined with the sentence above. ',
        '"And another quote that should also be combined with the sentence above. ',
        "A short sentence to be combined with the one above",
        "Short sentence to be combined with the one below. ",
        '"Another quote. ',
    ]

    expected_output = [1, 2, 2, 2, 3, 4, 4, 4, 4, 4, 5, 5]

    result = predictor(paragraphs)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"


def test_group_paragraphs_using_syntactic_features() -> None:
    """It groups paragraphs using the syntactic features."""
    paragraphs = [
        "Hello, world! ",
        "this is a long sentence that should not be combined with the one above",
        "* List item that is long but it should be combined with the one above",
        "* Another list item that is long but it should be combined with the one above",
        "this is a long sentence that should not be combined with the one above",
        "Ends in a colon:",
        "this is a long sentence but it should be combined with the one ending in colon above",
        '"This is a quote that is long but it should be combined with the sentence above. ',
        '"And another quote that should also be combined with the sentence above. ',
        "A short sentence to be combined with the one above",
        "Short sentence to be combined with the one below. ",
        '"Another quote. ',
    ]

    expected_output = [
        ["Hello, world! "],
        [
            "this is a long sentence that should not be combined with the one above",
            "* List item that is long but it should be combined with the one above",
            "* Another list item that is long but it should be combined with the one above",
        ],
        ["this is a long sentence that should not be combined with the one above"],
        [
            "Ends in a colon:",
            "this is a long sentence but it should be combined with the one ending in colon above",
            '"This is a quote that is long but it should be combined with the sentence above. ',
            '"And another quote that should also be combined with the sentence above. ',
            "A short sentence to be combined with the one above",
        ],
        [
            "Short sentence to be combined with the one below. ",
            '"Another quote. ',
        ],
    ]

    groups = split_model_train.group_paragraphs_using_syntactic_features(
        split_model_train.syntactic_paragraph_features, paragraphs
    )

    assert groups == expected_output, f"Expected {expected_output}, but got {groups}"


def test_predict_using_features_and_embeddings() -> None:
    """It predicts the splits for each paragraph using the syntactic features followed by embeddings."""

    def dummy_embedder(paragraphs: list[str]) -> list[NDArray[np.float32]]:
        embeddings = [
            np.array([0.5, 0.5], dtype=np.float32),
            np.array([0.6, 0.4], dtype=np.float32),
            np.array([0.7, 0.3], dtype=np.float32),
            np.array([0.6, 0.4], dtype=np.float32),
            np.array([0.4, 0.6], dtype=np.float32),
        ]
        return embeddings

    paragraphs = [
        "Hello, world! ",
        "this is a long sentence that should not be combined with the one above",
        "* List item that is long but it should be combined with the one above",
        "* Another list item that is long but it should be combined with the one above",
        "this is a long sentence that should not be combined with the one above",
        "Ends in a colon:",
        "this is a long sentence but it should be combined with the one ending in colon above",
        '"This is a quote that is long but it should be combined with the sentence above. ',
        '"And another quote that should also be combined with the sentence above. ',
        "A short sentence to be combined with the one above",
        "Short sentence to be combined with the one below. ",
        '"Another quote. ',
    ]

    threshold = 0.5

    expected_output = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2]

    predictor = split_model_train.predict_using_features_and_embeddings(
        split_model_train.syntactic_paragraph_features, dummy_embedder, threshold
    )

    result = predictor(paragraphs)

    assert result == expected_output, f"Expected {expected_output}, but got {result}"


class _Token(NamedTuple):
    pos_: str


class _Doc:
    def __iter__(self) -> Iterator[_Token]:
        return iter([_Token("WORD"), _Token("PUNCT"), _Token("WORD")])

    sents: list[str] = ["s1"]


def _dummy_parser(text: str) -> _Doc:
    return _Doc()


def test_predict_using_features_and_ensemble() -> None:
    """It predicts the splits for each paragraph using the syntactic features followed by embeddings."""

    def dummy_embedder(texts: list[str]) -> list[NDArray[np.float32]]:
        return [
            np.array([0.7, 0.7], dtype=np.float32),
            np.array([0.7, 0.7], dtype=np.float32),
            np.array([0.2, 0.2], dtype=np.float32),
        ]

    class DummyClf:
        def predict_proba(self, features: pd.DataFrame) -> list[list[float]]:
            return [[0.0, features["openai"][0]]]

    paragraphs = [
        "This is paragraph one. It should not be combined with any other paragraph.",
        "This is paragraph two. It should not be combined with any other paragraph.",
        "This is paragraph three. It should not be combined with any other paragraph.",
    ]

    threshold = 0.5

    predict = split_model_train.predict_using_features_and_ensemble(
        split_model_train.syntactic_paragraph_features,
        dummy_embedder,
        dummy_embedder,
        _dummy_parser,
        DummyClf(),
        threshold,
    )

    expected_output = [1, 1, 2]

    splits = predict(paragraphs)

    assert len(splits) == 3, f"Expected 3 splits, but got {len(splits)}"
    assert splits == expected_output, f"Expected splits {expected_output}, but got {splits}"


def test_count_words() -> None:
    """It counts the number of words in the paragraph."""
    tokens = [_Token("WORD"), _Token("PUNCT"), _Token("WORD")]

    assert split_model_train.count_words(tokens) == 2


def test_get_text_features() -> None:
    """It returns the text features for the paragraph."""
    expected_output = {
        "pre_tokens": 1 / (2 + 1),
        "pre_sentences": 1 / (1 + 1),
    }
    features = split_model_train.get_text_features("pre", "dummy", _dummy_parser)

    assert features == expected_output, f"Expected {expected_output}, but got {features}"


def test_get_pair_features() -> None:
    """It returns the features for the pair of paragraphs."""
    openai_embeds = [
        np.array([0.1, 0.2, 0.3], dtype=np.float32),
        np.array([0.4, 0.5, 0.6], dtype=np.float32),
    ]
    mpnet_embeds = [
        np.array([0.7, 0.8, 0.9], dtype=np.float32),
        np.array([1.0, 1.1, 1.2], dtype=np.float32),
    ]
    texts = ["Sample paragraph 1", "Sample paragraph 2"]

    features = split_model_train.get_pair_features(0, 1, openai_embeds, mpnet_embeds, _dummy_parser, texts)

    expected_features = {
        "openai": float(np.dot(openai_embeds[0], openai_embeds[1])),
        "mpnet": float(np.dot(mpnet_embeds[0], mpnet_embeds[1])),
        "left_tokens": 1 / (2 + 1),
        "left_sentences": 1 / (1 + 1),
        "right_tokens": 1 / (2 + 1),
        "right_sentences": 1 / (1 + 1),
    }
    assert features == expected_features, f"Expected {expected_features}, but got {features}"


def test_get_labeled_pairs() -> None:
    """It returns the labeled pairs of paragraphs."""

    def dummy_embedder(texts: list[str]) -> list[NDArray[np.float32]]:
        return [np.array([0.1, 0.2, 0.3], dtype=np.float32) for _ in texts]

    talk_sections = [
        {
            "paragraphs": [
                {
                    "text": "This is paragraph one. It should not be combined with any other paragraph.",
                    "split": 1,
                },
                {
                    "text": "This is paragraph two. It should not be combined with any other paragraph.",
                    "split": 1,
                },
                {
                    "text": "This is paragraph three. It should not be combined with any other paragraph.",
                    "split": 2,
                },
            ]
        }
    ]

    pairs = split_model_train.get_labeled_pairs(
        talk_sections,
        dummy_embedder,
        dummy_embedder,
        _dummy_parser,
        split_model_train.syntactic_paragraph_features,
    )

    assert len(pairs) == 2, f"Expected 1 pair, but got {len(pairs)}"
    assert pairs[0]["label"] == 1, f"Expected label 1, but got {pairs[0]['label']}"
    assert pairs[1]["label"] == 0, f"Expected label 0, but got {pairs[1]['label']}"


def test_get_paragraph_ngram_pairs() -> None:
    """It returns ngram pairs from the paragraph-splits."""
    tests = [
        (
            [
                {"text": "P1-1", "split": 1},
                {"text": "P2-1", "split": 1},
                {"text": "P3-2", "split": 2},
                {"text": "P4-2", "split": 2},
            ],
            [
                {
                    "ngrams_left": 1,
                    "ngrams_right": 1,
                    "text_left": "P1-1",
                    "text_right": "P2-1",
                    "label": 0,
                },
                {
                    "ngrams_left": 2,
                    "ngrams_right": 1,
                    "text_left": "P1-1\n\nP2-1",
                    "text_right": "P3-2",
                    "label": 1,
                },
                {
                    "ngrams_left": 2,
                    "ngrams_right": 2,
                    "text_left": "P1-1\n\nP2-1",
                    "text_right": "P3-2\n\nP4-2",
                    "label": 1,
                },
                {
                    "ngrams_left": 1,
                    "ngrams_right": 1,
                    "text_left": "P2-1",
                    "text_right": "P3-2",
                    "label": 1,
                },
                {
                    "ngrams_left": 1,
                    "ngrams_right": 2,
                    "text_left": "P2-1",
                    "text_right": "P3-2\n\nP4-2",
                    "label": 1,
                },
                {
                    "ngrams_left": 1,
                    "ngrams_right": 1,
                    "text_left": "P3-2",
                    "text_right": "P4-2",
                    "label": 0,
                },
            ],
        )
    ]
    for paragraph_splits, expected in tests:
        result = split_model_train.get_paragraph_ngram_pairs(paragraph_splits)
        assert result == expected
