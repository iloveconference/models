"""Utility functions for processing data."""

import os
import re
from typing import Generator


def get_filenames(directory: str) -> list[str]:
    """Get filenames in directory."""
    return [
        os.path.join(directory, f)
        for f in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, f))
    ]


def get_sections(text: str) -> Generator[tuple[str, str], None, None]:
    """Get sections in text as (section title, section text)."""
    section_title = ""
    for ix, region in enumerate(re.split(r"([^\n]+)\n-{4,}(?:\n|$)", text)):
        if ix % 2 == 1:
            section_title = region.strip()
        elif len(region.strip()) > 0:
            yield section_title, region.strip()
