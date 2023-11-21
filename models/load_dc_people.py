"""Load knowhys."""

from bs4 import BeautifulSoup
from langchain.schema.document import Document

from models.load_utils import clean
from models.load_utils import to_markdown


def load_dc_people(url: str, html: str, bs_parser: str = "html.parser") -> Document:
    """Load dc people from a url and html."""
    soup = BeautifulSoup(html, bs_parser)
    title = soup.find("h1", class_="elementor-heading-title")

    body = soup.find("div", class_="elementor-element-7c4c46d2")
    content = clean(to_markdown(str(body), base_url=url)) if body else ""

    metadata = {
        "url": url,
        "title": clean(title) if title else "",
    }
    return Document(page_content=content, metadata=metadata)
