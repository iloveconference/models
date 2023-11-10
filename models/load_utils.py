"""Utility functions for loading and saving data."""

import json
import re
from typing import Iterable
from typing import cast

from bs4 import NavigableString
from bs4 import Tag
from langchain.schema.document import Document
from markdownify import MarkdownConverter  # type: ignore


def clean(text: str) -> str:
    """Replace non-breaking space with normal space and remove surrounding whitespace."""
    text = text.replace(" ", " ").replace("\u200b", "").replace("\u200a", " ")
    text = re.sub(r"(\n\s*)+\n", "\n\n", text)
    text = re.sub(r" +\n", "\n", text)
    return text.strip()


def get_text(soup: Tag | NavigableString | None) -> str:
    """Get the text if its not none otherwise return empty string."""
    return "" if soup is None else soup.text


def to_markdown(html: str, base_url: str) -> str:
    """Convert html to markdown."""
    return cast(
        str,
        MarkdownConverter(
            heading_style="ATX",
            strip=["script", "style"],
            base_url=base_url,
        ).convert(html),
    )


def save_docs_to_jsonl(array: Iterable[Document], file_path: str) -> None:
    """Save documents to jsonl file."""
    with open(file_path, "w") as jsonl_file:
        for doc in array:
            jsonl_file.write(doc.json() + "\n")


def load_docs_from_jsonl(file_path: str) -> Iterable[Document]:
    """Load documents from jsonl file."""
    array = []
    with open(file_path) as jsonl_file:
        for line in jsonl_file:
            data = json.loads(line)
            obj = Document(**data)
            array.append(obj)
    return array
