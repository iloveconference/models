"""Load D&C Places."""

import re

from bs4 import BeautifulSoup
from langchain.schema.document import Document

from models.load_utils import clean
from models.load_utils import to_markdown


def remove_year_headers(text):
    """Define the regular expression pattern."""
    pattern = r"## \d{4}(-\d{4})?(\s+-{3,})?"

    # Use re.sub to replace matches with an empty string
    cleaned_text = re.sub(pattern, "", text)

    return cleaned_text


def places_clean(text: str) -> str:
    """Make key points a level 3 heading."""
    text = clean(text)
    text = text.replace("## Key Points", "### Key Points")
    return text


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
    title = clean(soup.find("div", class_="elementor-text-editor")).replace("/", "", 1)
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
            text = places_clean(to_markdown(str(section), base_url=url)) if section else ""
            text = replace_header_with_year(text)
            text = remove_year_headers(text)
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
