"""The document type the load, split, and index stages pass between each other."""

import json
from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class Document:
    """A piece of text and its metadata."""

    page_content: str
    metadata: dict[str, Any] = field(default_factory=dict)

    def json(self) -> str:
        """Serialize to a single-line json object."""
        return json.dumps({"page_content": self.page_content, "metadata": self.metadata})
