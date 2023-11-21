"""Load encyclopedia."""
from bs4 import BeautifulSoup
from langchain.schema.document import Document

from models.load_utils import clean
from models.load_utils import to_markdown


def load_encyclopedia(url: str, html: str, bs_parser: str = "html.parser") -> Document:
    """Load encyclopedia from a url and html."""
    soup = BeautifulSoup(html, bs_parser)
    title = soup.find("span", class_="mw-page-title-main")
    body = soup.find("div", class_="mw-parser-output")
    content = clean(to_markdown(str(body), base_url=url)) if body else ""

    metadata = {
        "url": url,
        "title": clean(title) if title else "",
    }
    return Document(page_content=content, metadata=metadata)
