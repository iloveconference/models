"""Utilities for indexing documents in Pinecone."""
import hashlib
import os
import time
from typing import Any
from typing import Optional

from openai import OpenAI
from tqdm.auto import tqdm

from models.document import Document


EMBEDDING_MODEL = "text-embedding-ada-002"


def get_doc_id(doc: Document) -> str:
    """Get a unique ID for a document."""
    # Create a SHA-256 hash object
    sha256 = hashlib.sha256()
    # hash the url (if it exists) + text
    text = doc.metadata.get("url", "") + "~" + doc.page_content
    # Update the hash object with the text's bytes
    sha256.update(text.encode("utf-8"))
    # Get the hexadecimal representation of the hash
    return sha256.hexdigest()


class OpenAIEmbedder:
    """Embed documents with an OpenAI embedding model.

    Replaces langchain.embeddings.openai.OpenAIEmbeddings: it exposes the embed_documents
    method that embed_documents below calls, backed directly by the openai 2.x client.
    """

    def __init__(
        self,
        model: str = EMBEDDING_MODEL,
        api_key: Optional[str] = None,
        client: Optional[OpenAI] = None,
    ) -> None:
        """Initialize the embedder.

        Args:
            model: name of the OpenAI embedding model. The production index is 1536-dim
                text-embedding-ada-002 and the live server embeds queries with the same
                model, so changing this silently destroys retrieval quality.
            api_key: OpenAI API key; defaults to the OPENAI_API_KEY environment variable.
            client: an already-configured OpenAI client; overrides api_key when given.
        """
        self.model = model
        if client is None:
            client = OpenAI(api_key=api_key if api_key is not None else os.environ["OPENAI_API_KEY"], max_retries=6)
        self.client = client

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        """Return one embedding per text, in the order the texts were given.

        Args:
            texts: the texts to embed; each must fit the model's 8191-token context,
                which the splitter's 2000-character chunks always do. langchain used to
                hide an over-long text by averaging token chunks; the raw API returns a
                400 instead.

        Returns:
            One 1536-float embedding per text.
        """
        response = self.client.embeddings.create(input=texts, model=self.model)
        return [record.embedding for record in sorted(response.data, key=lambda record: record.index)]

    def embed_query(self, text: str) -> list[float]:
        """Return the embedding of a single query text.

        Args:
            text: the text to embed.

        Returns:
            The 1536-float embedding of the text.
        """
        return self.embed_documents([text])[0]


def embed_documents(embedder: Any, docs: list[Document], batch_size: int = 100, delay: float = 1.0) -> list[Any]:
    """Return document embeddings using an embedder."""
    embeddings = []
    for i in tqdm(range(0, len(docs), batch_size)):
        # wait between batches
        time.sleep(delay)
        # set end position of batch
        i_end = min(i + batch_size, len(docs))
        text_batch = [f"{doc.metadata['title']}\n\n{doc.page_content}" for doc in docs[i:i_end]]
        embed_batch = embedder.embed_documents(text_batch)
        embeddings.extend(embed_batch)
    return embeddings


def index_documents(index: Any, embeddings: list[Any], docs: list[Document], batch_size: int = 100) -> None:
    """Index documents in Pinecone."""
    for i in tqdm(range(0, len(docs), batch_size)):
        # set end position of batch
        i_end = min(i + batch_size, len(docs))
        # get batch of lines and IDs
        metadata_batch = [
            dict(
                docs[n].metadata,
                text=docs[n].page_content,
                source=get_doc_id(docs[n]),
            )
            for n in range(i, i_end)
        ]
        ids_batch = [get_doc_id(doc) for doc in docs[i:i_end]]
        # get embeddings
        embed_batch = embeddings[i:i_end]
        # create upsert batch
        to_upsert = zip(ids_batch, embed_batch, metadata_batch, strict=True)
        # upsert to Pinecone
        index.upsert(vectors=list(to_upsert))
