"""Test cases for the data_utils module."""

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
            'To Moses, God declared, "I have a work for thee" ([Moses 1:6]). Have you ever wondered if Heavenly Father '
            + "has a work for you? Are there important things He has prepared you—and specifically you—to accomplish? "
            + "I testify the answer is yes!",
            "p3",
        ),
        (
            "Consider Girish Ghimire, who was born and raised in the country of Nepal. As a teenager, he studied in "
            + "China, where a classmate introduced him to the gospel of Jesus Christ. Eventually, Girish came to "
            + "Brigham Young University for graduate work and met his future wife. They settled in the Salt Lake "
            + "Valley and adopted two children from Nepal.",
            "p4",
        ),
        ('To Moses, God declared, "I have a work for thee" Test multiple anchors in the same paragraph.', "p5"),
    ]

    result = split_utils.get_paragraph_texts_and_ids(content)
    assert len(result) == 3
    assert result == expected


def test_get_split_texts_and_ids() -> None:
    """It returns splits."""
    paragraph_texts_and_ids = [
        ("This is paragraph 1", "anchor_1"),
        ("This is paragraph 2", "anchor_2"),
        ("This is paragraph 3", "anchor_3"),
        ("This is paragraph 4 with a lot of words", "anchor_4"),
        ("This is paragraph 5", "anchor_5"),
        ("This is paragraph 6", "anchor_6"),
    ]
    splits = [1, 1, 2, 2, 2, 3]

    expected_output = [
        ("This is paragraph 1\n\n\nThis is paragraph 2", "anchor_1"),
        ("This is paragraph 3", "anchor_3"),
        ("This is paragraph 3\n\n\nThis is paragraph 4 with a lot of words", "anchor_4"),
        ("This is paragraph 4 with a lot of words\n\n\nThis is paragraph 5", "anchor_5"),
        ("This is paragraph 6", "anchor_6"),
    ]

    result = split_utils.get_split_texts_and_ids(paragraph_texts_and_ids, splits, 10)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
