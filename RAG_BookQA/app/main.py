from __future__ import annotations

from typing import Any, Dict, List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from rag.chain import ask_question, build_conversational_chain
from rag.config import load_settings
from rag.vectorstore import load_faiss_index


class AskRequest(BaseModel):
    question: str = Field(..., description="User question in English or Bangla")
    language: Optional[str] = Field(
        default="auto", description="Preferred answer language: auto|en|bn"
    )


class AskResponse(BaseModel):
    answer: str
    sources: List[Dict[str, Any]]


app = FastAPI(title="RAG Book QA", version="1.0.0")


@app.on_event("startup")
def _on_startup() -> None:
    global chain
    settings = load_settings()
    try:
        vs = load_faiss_index(settings)
    except Exception as e:  # noqa: BLE001
        raise RuntimeError(
            "FAISS index is missing. Run the ingestion first: python -m scripts.ingest_pdfs"
        ) from e
    chain = build_conversational_chain(settings, vs)


@app.post("/ask", response_model=AskResponse)
def ask(request: AskRequest) -> AskResponse:
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question must not be empty")
    question_text = request.question
    lang = (request.language or "auto").lower()
    if lang == "en":
        question_text = "Please answer in English.\n" + question_text
    elif lang in {"bn", "bangla", "bengali"}:
        question_text = "অনুগ্রহ করে বাংলায় উত্তর দিন।\n" + question_text

    answer, sources = ask_question(chain, question_text)
    return AskResponse(answer=answer, sources=sources)


