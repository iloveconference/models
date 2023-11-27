"""Test cases for the data_utils module."""
import spacy

from models import split_utils


def test_get_filenames() -> None:
    """It returns filenames."""
    result = split_utils.get_filenames(".")
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

    result = list(split_utils.get_sections(text))
    assert len(result) == 3
    assert result[0][0] == ""
    assert result[0][1] == "intro"
    assert result[1][0] == "Section 1"
    assert result[1][1] == "line 1\nline 2"


def test_get_paragraph_texts_and_ids() -> None:
    """It returns paragraphs."""
    content = """
        <a name="p3"></a>To Moses, God declared, “I have a work for thee”
        ([Moses 1:6](https://www.churchofjesuschrist.org/study/scriptures/pgp/moses/1.6?lang=eng#p6)).
        Have you ever wondered if Heavenly Father has a work for you? Are there important things He has prepared
        you—and specifically you—to accomplish? I testify the answer is yes!


        ![]()  ImageGirish Gemera
        <a name="p4"></a>Consider Girish Ghimire, who was born and raised in the country of Nepal.
        As a teenager, he studied in China, where a classmate introduced him to the gospel of Jesus Christ.[1]
        Eventually, Girish came to Brigham Young University for graduate work and met his future wife.
        They settled in the Salt Lake Valley and adopted two children from Nepal.


        <a name="p5"></a>To Moses, God declared, “I have a work for thee”
        <a name="p6"></a>Test multiple anchors in the same paragraph.
        """

    expected = [
        (
            'To Moses, God declared, "I have a work for thee" (Moses 1:6). Have you ever wondered if Heavenly Father '
            + "has a work for you? Are there important things He has prepared you—and specifically you—to accomplish? "
            + "I testify the answer is yes!\n\n",
            "p3",
        ),
        (
            "Consider Girish Ghimire, who was born and raised in the country of Nepal. As a teenager, he studied in "
            + "China, where a classmate introduced him to the gospel of Jesus Christ. Eventually, Girish came to "
            + "Brigham Young University for graduate work and met his future wife. They settled in the Salt Lake "
            + "Valley and adopted two children from Nepal.\n\n",
            "p4",
        ),
        ('To Moses, God declared, "I have a work for thee" Test multiple anchors in the same paragraph.\n\n', "p5"),
    ]

    result = split_utils.get_paragraph_texts_and_ids(content)
    assert len(result) == 3
    assert result == expected


def test_get_split_texts_and_ids() -> None:
    """It returns splits."""
    paragraph_texts_and_ids = [
        ("This is paragraph 1\n\n", "anchor_1"),
        ("This is paragraph 2\n\n", "anchor_2"),
        ("This is paragraph 3\n\n", "anchor_3"),
        ("This is paragraph 4 with a lot of words\n\n", "anchor_4"),
        ("This is paragraph 5\n\n", "anchor_5"),
        ("This is paragraph 6\n\n", "anchor_6"),
    ]
    splits = [1, 1, 2, 2, 2, 3]

    expected_output = [
        ("This is paragraph 1\n\nThis is paragraph 2", "anchor_1"),
        ("This is paragraph 3", "anchor_3"),
        ("This is paragraph 3\n\nThis is paragraph 4 with a lot of words", "anchor_4"),
        ("This is paragraph 4 with a lot of words\n\nThis is paragraph 5", "anchor_5"),
        ("This is paragraph 6", "anchor_6"),
    ]

    result = split_utils.get_split_texts_and_ids(paragraph_texts_and_ids, splits, 10)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"


def test_get_paragraph_sentence_texts_and_ids() -> None:
    """It returns paragraphs, lines, or sentences (text, anchor) from contents."""
    parser = spacy.load("en_core_web_sm")
    max_chars = 120
    content = """
        <a name="p1"></a>To Moses, God declared, “I have a work for thee”
        Have you ever wondered if Heavenly Father has a work for you? Are there important things He has prepared
        you—and specifically you—to accomplish? I testify the answer is yes!

        <a name="p2"></a>To Moses, God declared, “I have a work for thee” This paragraph is short.
        New line.

        <a name="p3"></a>To Moses, God declared, “I have a work for thee.” This paragraph is long but it contains multiple sentences. This is the last sentence.
    """  # noqa: E731, B950

    results = split_utils.get_paragraph_sentence_texts_and_ids(content, parser, max_chars)
    assert len(results) == 7
    assert results[0] == ('To Moses, God declared, "I have a work for thee"\n', "p1")
    assert results[1] == (
        "Have you ever wondered if Heavenly Father has a work for you? Are there important things "
        + "He has prepared\n",
        "p1",
    )
    assert results[2] == ("you—and specifically you—to accomplish? I testify the answer is yes!\n\n", "p1")
    assert results[3] == (
        'To Moses, God declared, "I have a work for thee" This paragraph is short.\n New line.\n\n',
        "p2",
    )
    assert results[4] == ('To Moses, God declared, "I have a work for thee."', "p3")
    assert results[5] == ("This paragraph is long but it contains multiple sentences.", "p3")
    assert results[6] == ("This is the last sentence.\n\n", "p3")


def test_split_on_markdown_headers() -> None:
    """Is splits text on markdown headers."""
    max_chars = 10
    content = """
preamble
# Header 1
line 1
## Header 2
line 2
## Header 3

line 3
---
line 3a
## Header 4

line 4

**Bold header**

final line.
"""

    results = split_utils.split_on_markdown_headers(content, max_chars)
    assert len(results) == 7
    assert results[0] == "preamble\n"
    assert results[1] == "# Header 1\nline 1\n"
    assert results[2] == "## Header 2\nline 2\n"
    assert results[3] == "## Header 3\n\nline 3\n"
    assert results[4] == "line 3a\n"
    assert results[5] == "## Header 4\n\nline 4\n\n"
    assert results[6] == "**Bold header**\n\nfinal line.\n"


def test_clean_text() -> None:
    """It tests cleaning text."""
    text = """
        <a name="p1"></a>To Moses, [God](https://churchofjesuschrist.org) declared, “I have a work for thee”
        ![caption](https://image) Line 2
    """
    result = split_utils.clean_text(text)
    assert result == 'To Moses, God declared, "I have a work for thee" Line 2'
    result = split_utils.clean_text(text, keep_anchors=True, keep_newlines=True)
    assert result == '<a name="p1"></a>To Moses, God declared, "I have a work for thee"\n Line 2\n '
