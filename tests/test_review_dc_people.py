"""Test cases for the review_load_dc_people"""
"""
This test checks for text after '=========='
if it exists it will fail so that the text will
be removed or pass if it has already been removed
"""
# flake8: noqa

import re


mark_text = """


"""


def check_text(markdown_content):
    # result check variable boolean
    result_check = []

    # Search for the position of "abstract" (case insensitive)
    abstract_match = re.search(r"\b## ABSTRACT\b", markdown_content, re.IGNORECASE)

    if abstract_match:
        # Check content before the "abstract" text
        abstract_position = abstract_match.start()

        # Check if there is text before the "abstract" section
        if abstract_position > 0:
            result_check.append(True)
        else:
            result_check.append(False)

    else:
        result_check.append(False)

    return result_check


def test_review_load_dc_people() -> None:
    """It returns a valid Document for load dc people."""

    result = check_text(mark_text)
    assert len(result) == 2
    assert result[0] == False
    assert result[1] == False
