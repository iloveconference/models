"""Utilities for indexing documents in Pinecone."""
from typing import Any

from langchain.schema.document import Document
from tqdm.auto import tqdm


def index(index: Any, embedder: Any, docs: list[Document], batch_size: int = 100) -> None:
    """Index documents in Pinecone."""
    for i in tqdm(range(0, len(docs), batch_size)):
        # set end position of batch
        i_end = min(i + batch_size, len(docs))
        # get batch of lines and IDs
        metadata_batch = [
            dict(
                docs[n].metadata,
                text=docs[n].page_content,
                source=str(n),
            )
            for n in range(i, i_end)
        ]
        text_batch = [doc.page_content for doc in docs[i:i_end]]
        ids_batch = [str(n) for n in range(i, i_end)]
        # create embeddings
        embed_batch = embedder.embed_documents(text_batch)
        # create upsert batch
        to_upsert = zip(ids_batch, embed_batch, metadata_batch, strict=True)
        # upsert to Pinecone
        index.upsert(vectors=list(to_upsert))
