"""Load D&C Places."""

import json
import os
import re
from typing import Iterator
from typing import cast

from bs4 import BeautifulSoup  # type: ignore
from langchain.document_loaders.base import BaseLoader
from langchain.schema.document import Document
from markdownify import MarkdownConverter  # type: ignore
from tqdm import tqdm

from models.load_utils import clean


def places_clean(text: str) -> str:
    """Make key points a level 3 heading."""
    text = clean(text)
    text = text.replace("## Key Points", "### Key Points")
    return text


# Create shorthand method for custom conversion
def _to_markdown(html: str, base_url: str) -> str:
    """Convert html to markdown."""
    return cast(str, MarkdownConverter(heading_style="ATX", base_url=base_url).convert(html))


def replace_header_with_year(text: str) -> str:
    """Define a regular expression pattern to match any year range."""
    year_pattern = re.compile(r"\b\d{4}\s*-\s*\d{4}\b")  # Matches year ranges like 1828-1830, 1823 - 1830, etc.

    # Find the first occurrence of a year range in the text
    match = year_pattern.search(text)

    if match:
        # Replace the matched year range with an empty string
        modified_text = text[: match.start()] + text[match.end() :]
        return modified_text
    else:
        return text  # Return the original text if no year range is found


def load_dc_places(url: str, html: str, bs_parser: str = "html.parser") -> Document:
    """Load dc places from a url and html."""
    body = []
    soup = BeautifulSoup(html, bs_parser)
    title = soup.find("div", class_="elementor-text-editor").text
    title = title.replace("/", "", 1)
    sections = soup.find_all("section", class_="has_eae_slider")
    for section in sections:
        if (
            not section.find("div", class_="elementor-gallery-item__content")
            and not section.find("a", class_="e-gallery-item")
            and not section.find("div", class_="elementor-background-overlay")
            and not any("Significant Events At a Glance" in tag.text for tag in section.find_all("h2"))
            and not any("D&C Sections Received Here" in tag.text for tag in section.find_all("h2"))
            and not any("Take a 360°" in tag.text for tag in section.find_all("h2"))
            and not any("Photo Credit:" in tag.text for tag in section.find_all("h2"))
            and not any("(Tap photo to enlarge and see more information)" in tag.text for tag in section.find_all("h2"))
            and not any("Directions to" in tag.text for tag in section.find_all("h2"))
            and not section.find("a", href=True)
        ):
            text = places_clean(_to_markdown(str(section), base_url=url)) if section else ""
            text = replace_header_with_year(text)
            # print('text:',text)
            if text == "## ":
                continue
            body.append(text)
    content = "\n\n--------\n\n".join(body)
    metadata = {
        "url": url,
        "title": clean(title) if title else "",
        # "author": clean(author) if author else "",
    }
    return Document(page_content=content, metadata=metadata)


class PlacesLoader(BaseLoader):
    """Loader for D&C Places."""

    def lazy_load(self) -> Iterator[Document]:
        """A lazy loader for Documents."""
        raise NotImplementedError(f"{self.__class__.__name__} does not implement lazy_load()")

    def __init__(self, path: str = "", bs_parser: str = "html.parser"):
        """Initialize loader."""
        super().__init__()
        self.path = path
        self.bs_parser = bs_parser

    def load(self, verbose: bool = False) -> list[Document]:
        """Load documents from path."""
        docs = []
        for filename in tqdm(os.listdir(self.path), disable=not verbose):
            path = os.path.join(self.path, filename)
            with open(path, encoding="utf8") as f:
                data = json.load(f)
            doc = load_dc_places(data["url"], data["html"], bs_parser=self.bs_parser)
            if not doc.metadata["title"] or not doc.page_content:
                if verbose:
                    print("Missing title or content - skipping", filename)
                continue
            # if not doc.metadata["author"]:
            #     if verbose:
            #         print("Missing author", filename)
            docs.append(doc)
        return docs
