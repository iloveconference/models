"""Test cases for the index_utils module."""

from typing import Any
from typing import cast

import pytest
from openai import OpenAI

from models import index_utils
from models.document import Document


class _FakeRecord:
    """One record of a fake openai embeddings response."""

    __slots__ = ("index", "embedding")

    def __init__(self, index: int, embedding: list[float]) -> None:
        self.index = index
        self.embedding = embedding


class _FakeResponse:
    """A fake openai embeddings response."""

    __slots__ = ("data",)

    def __init__(self, data: list[_FakeRecord]) -> None:
        self.data = data


class _FakeEmbeddings:
    """The embeddings namespace of a fake openai client."""

    def __init__(self, owner: "_FakeClient") -> None:
        self.owner = owner

    def create(self, input: list[str], model: str) -> _FakeResponse:  # noqa: A002
        """Record the call and return one reversed-order record per input.

        Args:
            input: the texts to embed.
            model: the embedding model name.

        Returns:
            A response whose records are deliberately out of input order.
        """
        self.owner.calls.append({"input": list(input), "model": model})
        records = [_FakeRecord(ix, [float(ix), 0.5]) for ix in range(len(input))]
        return _FakeResponse(list(reversed(records)))


class _FakeClient:
    """A fake openai client that records the calls made to it."""

    def __init__(self) -> None:
        self.calls: list[dict[str, Any]] = []
        self.embeddings = _FakeEmbeddings(self)


def _embedder(client: _FakeClient, model: str = index_utils.EMBEDDING_MODEL) -> index_utils.OpenAIEmbedder:
    """Build an OpenAIEmbedder over a fake client."""
    return index_utils.OpenAIEmbedder(model=model, client=cast(OpenAI, client))


def test_embedding_model_is_ada_002() -> None:
    """The production index is ada-002, so the default must not drift."""
    assert index_utils.EMBEDDING_MODEL == "text-embedding-ada-002"
    assert index_utils.OpenAIEmbedder(client=cast(OpenAI, _FakeClient())).model == "text-embedding-ada-002"


def test_embed_documents_sends_one_request_and_sorts_by_index() -> None:
    """All texts go out in one request and come back in input order."""
    client = _FakeClient()

    embeddings = _embedder(client).embed_documents(["alpha", "beta", "gamma"])

    assert embeddings == [[0.0, 0.5], [1.0, 0.5], [2.0, 0.5]]
    assert client.calls == [{"input": ["alpha", "beta", "gamma"], "model": "text-embedding-ada-002"}]


def test_embed_query_returns_a_single_embedding() -> None:
    """A query embeds as a one-element batch."""
    client = _FakeClient()

    assert _embedder(client).embed_query("alpha") == [0.0, 0.5]
    assert client.calls[0]["input"] == ["alpha"]


def test_embed_documents_honors_an_explicit_model() -> None:
    """An explicit model name reaches the client."""
    client = _FakeClient()

    _embedder(client, model="text-embedding-3-small").embed_documents(["alpha"])

    assert client.calls[0]["model"] == "text-embedding-3-small"


def test_init_without_a_client_requires_an_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    """With no client and no key anywhere, construction fails loudly."""
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    with pytest.raises(KeyError):
        index_utils.OpenAIEmbedder()


def test_module_level_embed_documents_prefixes_the_title() -> None:
    """embed_documents sends the title, a blank line, then the text - how production was built."""
    client = _FakeClient()
    docs = [Document(page_content="the body", metadata={"title": "The Title", "url": "https://example.com/a"})]

    embeddings = index_utils.embed_documents(_embedder(client), docs, batch_size=100, delay=0.0)

    assert embeddings == [[0.0, 0.5]]
    assert client.calls[0]["input"] == ["The Title\n\nthe body"]
