from __future__ import annotations

from pathlib import Path
from typing import List

from langchain.docstore.document import Document
from langchain_community.vectorstores import FAISS

from .config import RAGSettings
from .embeddings import create_embeddings


def build_faiss_index(settings: RAGSettings, documents: List[Document]) -> FAISS:
    embeddings = create_embeddings(settings)
    vector_store = FAISS.from_documents(documents, embeddings)
    return vector_store


def save_faiss_index(vector_store: FAISS, directory: Path) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    vector_store.save_local(str(directory))


def load_faiss_index(settings: RAGSettings) -> FAISS:
    embeddings = create_embeddings(settings)
    return FAISS.load_local(
        str(settings.vectorstore_dir),
        embeddings,
        allow_dangerous_deserialization=True,
    )


