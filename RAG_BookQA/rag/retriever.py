from __future__ import annotations

from typing import List

from langchain_community.vectorstores import FAISS

from .config import RAGSettings


def create_retriever(settings: RAGSettings, vector_store: FAISS):
    return vector_store.as_retriever(search_kwargs={"k": settings.retrieval_k})


