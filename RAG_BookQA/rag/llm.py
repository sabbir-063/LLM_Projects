from __future__ import annotations

from langchain_google_genai import ChatGoogleGenerativeAI

from .config import RAGSettings


def create_llm(settings: RAGSettings) -> ChatGoogleGenerativeAI:
    if not settings.google_api_key:
        raise RuntimeError("GOOGLE_API_KEY is not set. Please configure it in your environment.")

    return ChatGoogleGenerativeAI(
        model=settings.gemini_model_name,
        google_api_key=settings.google_api_key,
        temperature=settings.model_temperature,
    )


