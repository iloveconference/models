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


def load_fair(url: str, html: str, bs_parser: str = "html.parser") -> Document:
    """Load fair from a url and html."""
    soup = BeautifulSoup(html, bs_parser)
    title = soup.find("span", class_="mw-headline")
    body = soup.find("div", id="mw-content-text")
    content = clean(to_markdown(str(body), base_url=url)) if body else ""

    metadata = {
        "url": url,
        "title": clean(title) if title else "",
    }
    return Document(page_content=content, metadata=metadata)


class FairLoader(BaseLoader):
    """Loader for Fair."""

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
            doc = load_fair(data["url"], data["html"], bs_parser=self.bs_parser)
            if not doc.metadata["title"] or not doc.page_content:
                if verbose:
                    print("Missing title or content - skipping", filename)
                continue
            # if not doc.metadata["author"]:
            #     if verbose:
            #         print("Missing author", filename)
            docs.append(doc)
        return docs
