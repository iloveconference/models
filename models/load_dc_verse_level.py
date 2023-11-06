"""Load D&C Verse-Level Commentary."""

import json
import os
import re
from typing import Iterator
from typing import Optional

from bs4 import BeautifulSoup  # type: ignore
from langchain.document_loaders.base import BaseLoader
from langchain.schema.document import Document
from tqdm import tqdm

from models.load_utils import clean
from models.load_utils import to_markdown


def get_title(soup: BeautifulSoup) -> Optional[str]:
    """Gets page title."""
    # Find the first <section> element
    first_section = soup.find("section")

    # Check if a <section> element was found
    if not first_section:
        return None

    # Find the first <h2> element within the <section>
    first_h2 = first_section.find("h2")

    if not first_h2:
        return None

    return str(first_h2.get_text())  # Return the text of the first <h2> element


def get_content(soup: BeautifulSoup) -> Optional[BeautifulSoup]:
    """Gets page content."""
    # Find all <section> elements in the HTML
    sections = soup.find_all("section")

    # Check if there are at least three <section> elements
    if len(sections) < 3:
        return None

    # Return the first div with class elementor-widget inside the third section
    div = sections[2].find("div", class_="elementor-widget")
    return div


def convert_verses_to_headings(content: str) -> str:
    """Convert Verse N or Verses X-Y to level 2 markdown headings."""
    content = re.sub(r"(?:^|\n) *Verse (\d+) *\n", r"\n## Verse \1\n", content)
    content = re.sub(r"(?:^|\n) *Verses (\d+)-(\d+) *\n", r"\n## Verses \1-\2\n", content)
    return content.strip()


def load_dc_verse_level(url: str, html: str, bs_parser: str = "html.parser") -> Document:
    """Load knowhys from a url and html."""
    soup = BeautifulSoup(html, bs_parser)
    title = get_title(soup)
    body = get_content(soup)
    content = clean(to_markdown(str(body), base_url=url)) if body else ""
    content = convert_verses_to_headings(content)

    metadata = {
        "url": url,
        "title": clean(title) if title else "",
    }
    return Document(page_content=content, metadata=metadata)


class DcVerseLoader(BaseLoader):
    """Loader for General Conference Talks."""

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
            doc = load_dc_verse_level(data["url"], data["html"], bs_parser=self.bs_parser)
            if not doc.metadata["title"] or not doc.page_content:
                if verbose:
                    print("Missing title or content - skipping", filename)
                continue
            docs.append(doc)
        return docs
