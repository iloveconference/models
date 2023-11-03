"""Load podcasts."""

import json
import os
from typing import Any
from typing import Iterator
from typing import cast

from bs4 import BeautifulSoup  # type: ignore
from langchain.document_loaders.base import BaseLoader
from langchain.schema.document import Document
from markdownify import MarkdownConverter  # type: ignore
from tqdm import tqdm

from urllib.parse import urljoin, urlparse

from models.load_utils import clean


# Create shorthand method for custom conversion
def _to_markdown(html: str, **options: Any) -> str:
    """Convert html to markdown."""
    return cast(str, MarkdownConverter(**options).convert(html))


def load_dc_podcasts(url: str, html: str, bs_parser: str = "html.parser") -> Document:
    """Load dc podcasts from a url and html."""

    path_components = urlparse(url).path.split('/')
    title = path_components[-1]
    title = title.replace('-',' ')
    title = title.capitalize()
    content = clean(_to_markdown(html, base_url=url)) if html else ""

    metadata = {
        "url": url,
        "title": clean(title) if title else "",
    }
    return Document(page_content=content, metadata=metadata)


def get_text_of_third_h2_in_second_div(html_content):
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    # Find all div elements with class ‘elementor-col-50’
    div_elements = soup.find_all('div', class_='elementor-col-50')
    # Check if there is at least one div with the specified class
    if len(div_elements) >= 2:
        # Get the second div with class ‘elementor-col-50’
        second_div = div_elements[1]
        # Find all h2 elements within the second div
        h2_elements = second_div.find_all('h2')
        # Check if there is at least a third h2 element
        if len(h2_elements) >= 3:
            # Get the text of the third h2 element
            third_h2_text = h2_elements[2].get_text()
            return third_h2_text
    # If the structure is not found, return None or an appropriate message
    return None

def get_html_of_second_section_under_eael_tabs_content(html_content):
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    # Find all div elements with class ‘eael-tabs-content’
    div_elements = soup.find_all('div', class_='eael-tabs-content')
    # Check if there is at least one div with the specified class
    if len(div_elements) >= 1:
        # Get the first div with class ‘eael-tabs-content’
        target_div = div_elements[0]
        # Find all sections within the target div
        section_elements = target_div.find_all('section')
        # Check if there is at least a second section
        if len(section_elements) >= 2:
            # Get the second section
            second_section = section_elements[1]
            # Extract the HTML of the second section
            second_section_html = str(second_section)
            return second_section_html
    # If the structure is not found, return None or an appropriate message
    return None


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
