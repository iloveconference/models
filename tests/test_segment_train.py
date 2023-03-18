"""Test cases for the segment_train module."""

from models import segment_train


def test_get_paragraph_ngram_pairs() -> None:
    """It returns ngram pairs from the paragraph-segments."""
    tests = [
        (
            [
                {"text": "P1-1", "segment": 1},
                {"text": "P2-1", "segment": 1},
                {"text": "P3-2", "segment": 2},
                {"text": "P4-2", "segment": 2},
            ],
            [
                {
                    "ngrams_left": 1,
                    "ngrams_right": 1,
                    "text_left": "P1-1",
                    "text_right": "P2-1",
                    "label": 1,
                },
                {
                    "ngrams_left": 2,
                    "ngrams_right": 1,
                    "text_left": "P1-1\n\nP2-1",
                    "text_right": "P3-2",
                    "label": 0,
                },
                {
                    "ngrams_left": 2,
                    "ngrams_right": 2,
                    "text_left": "P1-1\n\nP2-1",
                    "text_right": "P3-2\n\nP4-2",
                    "label": 0,
                },
                {
                    "ngrams_left": 1,
                    "ngrams_right": 1,
                    "text_left": "P2-1",
                    "text_right": "P3-2",
                    "label": 0,
                },
                {
                    "ngrams_left": 1,
                    "ngrams_right": 2,
                    "text_left": "P2-1",
                    "text_right": "P3-2\n\nP4-2",
                    "label": 0,
                },
                {
                    "ngrams_left": 1,
                    "ngrams_right": 1,
                    "text_left": "P3-2",
                    "text_right": "P4-2",
                    "label": 1,
                },
            ],
        )
    ]
    for paragraph_segments, expected in tests:
        result = segment_train.get_paragraph_ngram_pairs(paragraph_segments)
        assert result == expected
