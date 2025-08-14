from __future__ import annotations

from pathlib import Path
from typing import List

from langchain.docstore.document import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

from .config import RAGSettings


def _load_single_pdf(pdf_path: Path) -> List[Document]:
    loader = PyPDFLoader(str(pdf_path))
    return loader.load()


def load_pdfs(settings: RAGSettings) -> List[Document]:
    documents: List[Document] = []
    for pdf_file in sorted(settings.pdf_dir.glob("*.pdf")):
        documents.extend(_load_single_pdf(pdf_file))
    return documents


def split_documents(settings: RAGSettings, documents: List[Document]) -> List[Document]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap,
        separators=["\n\n", "\n", "।", ".", " ", ""],  # include Bangla danda
    )
    return splitter.split_documents(documents)


