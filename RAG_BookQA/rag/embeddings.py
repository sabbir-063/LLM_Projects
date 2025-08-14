from __future__ import annotations

from langchain_google_genai import GoogleGenerativeAIEmbeddings

from .config import RAGSettings


def create_embeddings(settings: RAGSettings) -> GoogleGenerativeAIEmbeddings:
    if not settings.google_api_key:
        raise RuntimeError("GOOGLE_API_KEY is not set. Please configure it in your environment.")

    return GoogleGenerativeAIEmbeddings(
        model=settings.embedding_model_name,
        google_api_key=settings.google_api_key,
    )


