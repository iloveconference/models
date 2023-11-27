"""Crawl utils."""
import json
import time
from typing import Optional
from typing import Tuple

import requests


def get_page(
    url: str,
    delay_seconds: int = 30,
    headers: Optional[dict[str, str]] = None,
    encoding: str = "utf-8",
    timeout: int = 30,
) -> Tuple[int, str]:
    """Get page from url."""
    if headers is None:
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",  # noqa: B950
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9",
            "Sec-Ch-Ua": '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Linux"',
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",  # noqa: B950
        }
    response = requests.get(url, headers=headers, timeout=timeout)
    time.sleep(delay_seconds)
    if encoding:
        response.encoding = encoding
    return response.status_code, response.text


def save_page(path: str, url: str, html: str, encoding: str = "utf-8") -> None:
    """Save page url and html to path."""
    page_info = {
        "url": url,
        "html": html,
    }
    with open(path, "w", encoding=encoding) as f:
        json.dump(page_info, f, ensure_ascii=False, indent=2)
