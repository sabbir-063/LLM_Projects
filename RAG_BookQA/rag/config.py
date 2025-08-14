from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


@dataclass(frozen=True)
class RAGSettings:
    project_root: Path
    data_dir: Path
    pdf_dir: Path
    vectorstore_dir: Path
    google_api_key: str
    gemini_model_name: str
    embedding_model_name: str
    chunk_size: int
    chunk_overlap: int
    retrieval_k: int
    model_temperature: float


def load_settings() -> RAGSettings:
    load_dotenv()  # Load .env if present

    project_root = Path(__file__).resolve().parents[1]
    data_dir = project_root / "data"
    pdf_dir = data_dir / "pdfs"
    vectorstore_dir = data_dir / "vectorstore"

    google_api_key = os.getenv("GOOGLE_API_KEY", "")
    gemini_model_name = os.getenv("GEMINI_MODEL_NAME", "gemini-2.5-pro")
    embedding_model_name = os.getenv("EMBEDDING_MODEL_NAME", "text-embedding-004")
    chunk_size = int(os.getenv("CHUNK_SIZE", "1000"))
    chunk_overlap = int(os.getenv("CHUNK_OVERLAP", "200"))
    retrieval_k = int(os.getenv("RETRIEVAL_K", "5"))
    model_temperature = float(os.getenv("MODEL_TEMPERATURE", "0.2"))

    # Ensure dirs exist
    data_dir.mkdir(parents=True, exist_ok=True)
    pdf_dir.mkdir(parents=True, exist_ok=True)
    vectorstore_dir.mkdir(parents=True, exist_ok=True)

    return RAGSettings(
        project_root=project_root,
        data_dir=data_dir,
        pdf_dir=pdf_dir,
        vectorstore_dir=vectorstore_dir,
        google_api_key=google_api_key,
        gemini_model_name=gemini_model_name,
        embedding_model_name=embedding_model_name,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        retrieval_k=retrieval_k,
        model_temperature=model_temperature,
    )


