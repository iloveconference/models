"""Test cases for the data_utils module."""

from models import load_utils


def test_clean() -> None:
    """It cleans text."""
    text = "  This is a test.  "
    result = load_utils.clean(text)
    assert result == "This is a test."
