"""Load conference talks."""

import json
import os
from typing import Any
from typing import Iterator
from typing import cast
from urllib.parse import urljoin
from urllib.parse import urlparse

from bs4 import BeautifulSoup  # type: ignore
from langchain.document_loaders.base import BaseLoader
from langchain.schema.document import Document
from markdownify import MarkdownConverter  # type: ignore
from tqdm import tqdm


# Create shorthand method for custom conversion
def _to_markdown(html: str, **options: Any) -> str:
    """Convert html to markdown."""
    return cast(str, MarkdownConverter(**options).convert(html))


def _clean(text: str) -> str:
    """Replace non-breaking space with normal space."""
    # return text.replace(" ", " ")
    return text


def load_knowhy(url: str, html: str, bs_parser: str = "html.parser") -> Document:
    """Load a conference talk from a url and html."""
    soup = BeautifulSoup(html, bs_parser)
    title = soup.find("h1", class_ = "page-title").text
    author = soup.find("div", class_ = "field-nam-author").text
    author = author.replace("Post contributed by", author).strip()
    date = soup.find("div", class_ = "field-name-publish-date").text
    citation = soup.find(id="block-views-knowhy-citation-block")
    body = soup.find("div", class_ = "group-left")
    content = _clean(_to_markdown(str(body), base_url=url)) if body else ""

    metadata = {
        "url": url,
        "title": _clean(title) if title else "",
        "author": _clean(author) if author else "",
        "date": _clean(date) if date else "",
        "citation": _clean(_to_markdown(str(citation), base_url=url)) if citation else ""
    }
    return Document(page_content=content, metadata=metadata)


class KnowhyLoader(BaseLoader):
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
                print(data)
            doc = load_knowhy(data["url"], data["html"], bs_parser=self.bs_parser)
            if not doc.metadata["title"] or not doc.page_content:
                if verbose:
                    print("Missing title or content - skipping", filename)
                continue
            if not doc.metadata["author"]:
                if verbose:
                    print("Missing author", filename)
            docs.append(doc)
        return docs
