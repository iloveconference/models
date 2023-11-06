"""Load podcasts."""

import json
import os
from typing import Iterator
from typing import Optional

from bs4 import BeautifulSoup  # type: ignore
from langchain.document_loaders.base import BaseLoader
from langchain.schema.document import Document
from tqdm import tqdm

from models.load_utils import clean, to_markdown


def extract_title(soup: BeautifulSoup) -> Optional[str]:
    """Extract the title from the page."""
    # get the first section
    section = soup.find("section")
    # get the second div with class elementor-col-50
    divs = section.find_all("div", class_="elementor-col-50")
    if len(divs) < 2:
        return None
    # get the third h2 from this div
    h2s = divs[1].find_all("h2")
    if len(h2s) < 3:
        return None
    # get the text from this h2
    return str(h2s[2].text)


def extract_content(soup: BeautifulSoup) -> Optional[BeautifulSoup]:
    """Extract the HTML content from the page."""
    # Find all sections
    sections = soup.find_all("section")

    # check that there are at least 5 sections
    if len(sections) < 5:
        return None

    # return the sixth section
    return sections[4]


def load_dc_podcasts(url: str, html: str, bs_parser: str = "html.parser") -> Document:
    """Load dc podcasts from a url and html."""
    soup = BeautifulSoup(html, "html.parser")
    title = extract_title(soup)
    content = extract_content(soup)

    content = clean(to_markdown(str(content), base_url=url)) if content else ""

    metadata = {
        "url": url,
        "title": clean(title) if title else "",
    }
    return Document(page_content=content, metadata=metadata)


class PodcastsLoader(BaseLoader):
    """Loader for D&C Podcasts."""

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
            doc = load_dc_podcasts(data["url"], data["html"], bs_parser=self.bs_parser)
            if not doc.metadata["title"] or not doc.page_content:
                if verbose:
                    print("Missing title or content - skipping", filename)
                continue

            docs.append(doc)
        return docs
