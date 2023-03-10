"""Test cases for the data_utils module."""

from models import data_utils


def test_get_filenames() -> None:
    """It returns filenames."""
    result = data_utils.get_filenames(".")
    assert len(result) > 0


def test_get_sections() -> None:
    """It returns sections."""
    text = """
intro

Section 1
----

line 1
line 2

Section 2
----

line 3
line 4
    """

    result = list(data_utils.get_sections(text))
    assert len(result) == 3
    assert result[0][0] == ""
    assert result[0][1] == "intro"
    assert result[1][0] == "Section 1"
    assert result[1][1] == "line 1\nline 2"
