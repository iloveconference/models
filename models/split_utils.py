"""Utilities for splitting text into paragraphs and sections."""
import os
import re
from typing import Any
from typing import Generator
from typing import NamedTuple
from typing import Optional


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


def get_split_texts_and_ids(
    paragraph_texts_and_ids: list[tuple[str, str]], split_ixs: list[int], max_split_len: int
) -> list[tuple[str, str]]:
    """Group paragraphs into splits, and use the earliest anchor as the split ID."""
    splits = []
    curr_split_id = ""
    curr_split_ix = 0
    curr_split: list[str] = []
    for (paragraph, _id), split_ix in zip(paragraph_texts_and_ids, split_ixs, strict=True):
        if split_ix != curr_split_ix or _count_words(curr_split) + _count_words([paragraph]) > max_split_len:
            if len(curr_split) > 0:
                splits.append(("\n\n\n".join(curr_split), curr_split_id))
            if split_ix == curr_split_ix:
                curr_split = [curr_split[-1]]  # overlap
            else:
                curr_split = []
            curr_split_id = ""
            curr_split_ix = split_ix
        if curr_split_id == "" and _id != "":
            curr_split_id = _id
        curr_split.append(paragraph)
    if len(curr_split) > 0:
        splits.append(("\n\n\n".join(curr_split), curr_split_id))
    return splits


class Annotation(NamedTuple):
    """Annotation."""

    start: int
    end: int
    label: str


def get_annotations(annotations_in: list[dict[str, Any]]) -> list[Annotation]:
    """Get annotations from annotations_in."""
    # gather all results
    results = []
    for annotation in annotations_in:
        for result in annotation["result"]:
            if len(result["value"]["labels"]) != 1:
                raise ValueError("should be one label", len(result["value"]["labels"]))
            results.append(result)
    # create annotations from sorted results
    annotations = []
    start: Optional[int] = None
    label: Optional[str] = None
    end: Optional[int] = None
    for result in sorted(results, key=lambda res: res["value"]["start"]):
        if label != result["value"]["labels"][0]:
            if label is not None:
                # save previous split
                assert start is not None
                assert end is not None
                annotations.append(Annotation(start, end, label))
            start = result["value"]["start"]
            label = result["value"]["labels"][0]
        end = result["value"]["end"]
    if label is not None:
        # save final split
        assert start is not None
        assert end is not None
        annotations.append(Annotation(start, end, label))
    return annotations


def get_label_for_paragraph(start: int, end: int, annotations: list[Annotation]) -> str:
    """Get label for paragraph."""
    for annotation in annotations:
        # fuzzy match in case boundaries are off by a bit
        if start >= annotation.start - 3 and end <= annotation.end + 3:
            return annotation.label
    raise ValueError("annotation not found", start, end, annotations)


def get_paragraph_splits(annotations: list[Annotation], text: str) -> list[dict[str, Any]]:
    """Split text into paragraphs, and assign a split ID to each paragraph."""
    paragraph_splits = []
    start = 0
    split = 0
    prev_label = None
    for ix, paragraph in enumerate(re.split(r"(\n{2,})", text)):
        if ix % 2 == 1:
            start += len(paragraph)
            continue
        end = start + len(paragraph)
        label = get_label_for_paragraph(start, end, annotations)
        if label != prev_label:
            prev_label = label
            split += 1
        paragraph_splits.append(
            {
                "text": paragraph.strip(),
                "split": split,
            }
        )
        start = end
    return paragraph_splits
