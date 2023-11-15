"""Load fair."""

import json
import os
from typing import Iterator

from bs4 import BeautifulSoup
from langchain.document_loaders.base import BaseLoader
from langchain.schema.document import Document
from tqdm import tqdm

from models.load_utils import clean
from models.load_utils import to_markdown


def load_fairs(url: str, html: str, bs_parser: str = "html.parser") -> Document:
    """Load fairs from a url and html."""
    soup = BeautifulSoup(html, bs_parser)
    title = soup.find("span", class_="mw-headline")
    # author = clean(soup.find("div", class_="field-nam-author")).replace("Post contributed by", "")
    # date = soup.find("div", class_="field-name-publish-date")
    # citation = soup.find(id="block-views-knowhy-citation-block")
    body = soup.find("div", id="mw-content-text")
    # soup = BeautifulSoup(html, 'html.parser')
    # content = soup.find(...)
    title = body.find("span", class_="mw-headline")
    title.extract()
    content = clean(to_markdown(str(body), base_url=url)) if body else ""

    metadata = {
        "url": url,
        "title": clean(title) if title else "",
        # "author": clean(author) if author else "",
        # "date": clean(date) if date else "",
        # "citation": clean(to_markdown(str(citation), base_url=url)) if citation else "",
    }
    return Document(page_content=content, metadata=metadata)


class FairsLoader(BaseLoader):
    """Loader for fair."""

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
            doc = load_fairs(data["url"], data["html"], bs_parser=self.bs_parser)
            if not doc.metadata["title"] or not doc.page_content:
                if verbose:
                    print("Missing title or content - skipping", filename)
                continue
            # if not doc.metadata["author"]:
            #     if verbose:
            #         print("Missing author", filename)
            docs.append(doc)
        return docs
