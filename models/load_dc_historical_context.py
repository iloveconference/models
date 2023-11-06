"""Load knowhys."""

import json
import os
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
    if first_section:
        # Find the first <h2> element within the <section>
        first_h2 = first_section.find("h2")

        # Check if a <h2> element was found within the <section>
        if first_h2:
            return str(first_h2.get_text())  # Return the text of the first <h2> element
        else:
            return None  # No <h2> element found within the <section>
    else:
        return None  # No <section> element found in the HTML


def get_content(soup: BeautifulSoup) -> Optional[BeautifulSoup]:
    """Gets page content."""
    # Find all <section> elements in the HTML
    sections = soup.find_all("section")

    # Check if there are at least two <section> elements
    if len(sections) < 2:
        return None

    # Get the divs with class elemenetor-col-50
    divs = sections[1].find_all("div", class_="elementor-col-50")

    # Check if there are at least two divs with class elemenetor-col-50
    if len(divs) < 2:
        return None

    # Return the second div
    return divs[1]


def load_dc_historical_context(url: str, html: str, bs_parser: str = "html.parser") -> Document:
    """Load knowhys from a url and html."""
    soup = BeautifulSoup(html, bs_parser)
    title = get_title(soup)
    body = get_content(soup)
    content = clean(to_markdown(str(body), base_url=url)) if body else ""

    metadata = {
        "url": url,
        "title": clean(title) if title else "",
    }
    return Document(page_content=content, metadata=metadata)


class DcHistoricalLoader(BaseLoader):
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
            doc = load_dc_historical_context(data["url"], data["html"], bs_parser=self.bs_parser)
            if not doc.metadata["title"] or not doc.page_content:
                if verbose:
                    print("Missing title or content - skipping", filename)
                continue
            docs.append(doc)
        return docs
