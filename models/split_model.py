"""Split documents using upon a trained model."""

import os
import pickle
from typing import Any
from typing import Sequence

import openai
import spacy
from langchain.schema.document import BaseDocumentTransformer
from langchain.schema.document import Document
from sentence_transformers import SentenceTransformer  # type: ignore
from tqdm.autonotebook import tqdm

from models.split_model_train import get_mpnet_embedder
from models.split_model_train import get_openai_embedder
from models.split_model_train import predict_using_features_and_ensemble
from models.split_model_train import syntactic_paragraph_features
from models.split_utils import get_paragraph_texts_and_ids
from models.split_utils import get_split_texts_and_ids


class ModelTextSplitter(BaseDocumentTransformer):
    """Split documents using upon a trained model."""

    def __init__(
        self,
        model_path: str = "",
        split_threshold: float = 0.55,
        chunk_size: int = 500,
        anchor: str = "anchor",
        **kwargs: Any
    ):
        """Initialize splitter with model."""
        super(BaseDocumentTransformer, self).__init__(**kwargs)

        self.chunk_size = chunk_size
        self.anchor = anchor

        # load model
        with open(model_path, "rb") as f:  # nosec B301
            clf = pickle.load(f)

        # init spacy
        parser = spacy.load("en_core_web_sm")

        # load mpnet embedder for splitter
        mpnet = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")
        mpnet_embedder = get_mpnet_embedder(mpnet)

        # openai embedder for splitter
        openai.api_key = os.environ["OPENAI_API_KEY"]
        openai_embedder = get_openai_embedder(openai)

        self.predictor = predict_using_features_and_ensemble(
            syntactic_paragraph_features,
            openai_embedder,
            mpnet_embedder,
            parser,
            clf,
            split_threshold,
        )

    def transform_documents(self, documents: Sequence[Document], **kwargs: Any) -> Sequence[Document]:
        """Transform documents by splitting them using model."""
        verbose = kwargs.get("verbose", False)
        transformed: list[Document] = []
        for doc in tqdm(documents, disable=not verbose):
            # get paragraphs
            paragraph_texts_and_ids = get_paragraph_texts_and_ids(doc.page_content)
            paragraphs = [paragraph_text_id[0] for paragraph_text_id in paragraph_texts_and_ids]

            # get splits
            splits = self.predictor(paragraphs)
            split_texts_and_ids = get_split_texts_and_ids(
                paragraph_texts_and_ids,
                splits,
                max_split_len=self.chunk_size,
            )

            # create split
            for split_text_and_id in split_texts_and_ids:
                if self.anchor:
                    metadata = doc.metadata.copy()
                    metadata[self.anchor] = split_text_and_id[1]
                else:
                    metadata = doc.metadata
                transformed.append(Document(metadata=metadata, page_content=split_text_and_id[0]))
        return transformed

    async def atransform_documents(self, documents: Sequence[Document], **kwargs: Any) -> Sequence[Document]:
        """Transform documents asynchronously."""
        raise NotImplementedError

    def split_documents(self, documents: Sequence[Document], verbose: bool = False) -> list[Document]:
        """Split documents using model."""
        return list(self.transform_documents(documents, verbose=verbose))
