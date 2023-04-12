"""Utility functions for processing data."""

import os
import re
from typing import Generator


def get_filenames(directory: str) -> list[str]:
    """Get filenames in directory."""
    return [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]


def get_sections(text: str) -> Generator[tuple[str, str], None, None]:
    """Get sections in text as (section title, section text)."""
    section_title = ""
    for ix, region in enumerate(re.split(r"([^\n]+)\n-{4,}(?:\n|$)", text)):
        if ix % 2 == 1:
            section_title = region.strip()
        elif len(region.strip()) > 0:
            yield section_title, region.strip()


def clean_text(text: str) -> str:
    """Clean text: remove headers, images, links, anchors, and extra whitespace."""
    # remove headers
    text = re.sub(r"[^\n]+\n-{4,}(\n|$)", "", text)
    # remove images
    text = re.sub(r"!\[\]\(\)\s+Image[^\n]+\n", "", text)
    # remove links
    text = re.sub(r"(\[[^\]]+\])\([^\)]+\)", r"\1", text)
    # remove anchors
    text = re.sub(r"<a name=\"[^\"]+\"></a>", "", text)
    # remove citations
    text = re.sub(r"\[[0-9]+\]", "", text)
    # convert fancy quotes to quotes
    text = re.sub(r"[‘’]", "'", text)
    text = re.sub(r"[“”]", '"', text)
    # convert nbsp and zero-width space to space
    text = text.replace("\u00a0", " ").replace("\u200b", " ")
    # remove newlines and tabs
    text = text.replace("\n", " ").replace("\r", " ").replace("\t", " ")
    # remove extra whitespace
    text = re.sub(r"\s+", " ", text)
    # strip
    text = text.strip()
    return text


def get_paragraph_id(paragraph: str) -> str:
    """Get paragraph ID."""
    match = re.search(r'<a name="(.*?)"', paragraph)
    if match:
        anchor_name = match.group(1)
        return anchor_name
    return ""


def get_paragraph_texts_and_ids(contents: str) -> list[tuple[str, str]]:
    """Get paragraphs (text, anchor) from contents."""
    paragraphs = []
    for paragraph in contents.split("\n\n\n"):
        _id = get_paragraph_id(paragraph)
        paragraph = clean_text(paragraph)
        if not paragraph:
            continue
        paragraphs.append((paragraph, _id))
    return paragraphs


def _count_words(texts: list[str]) -> int:
    """Count words in texts."""
    return sum(len(text.split()) for text in texts)


def get_segment_texts_and_ids(
    paragraph_texts_and_ids: list[tuple[str, str]], segmentation: list[int], max_segment_len: int
) -> list[tuple[str, str]]:
    """Group paragraphs into segments, and use the earliest anchor as the segment ID."""
    segments = []
    curr_segment_id = ""
    curr_segment_ix = 0
    curr_segment: list[str] = []
    for (paragraph, _id), segment_ix in zip(paragraph_texts_and_ids, segmentation, strict=True):
        if segment_ix != curr_segment_ix or _count_words(curr_segment) + _count_words([paragraph]) > max_segment_len:
            if len(curr_segment) > 0:
                segments.append(("\n\n\n".join(curr_segment), curr_segment_id))
            if segment_ix == curr_segment_ix:
                curr_segment = [curr_segment[-1]]  # overlap
            else:
                curr_segment = []
            curr_segment_id = ""
            curr_segment_ix = segment_ix
        if curr_segment_id == "" and _id != "":
            curr_segment_id = _id
        curr_segment.append(paragraph)
    if len(curr_segment) > 0:
        segments.append(("\n\n\n".join(curr_segment), curr_segment_id))
    return segments
