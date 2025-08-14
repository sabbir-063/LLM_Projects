from __future__ import annotations

from rag.config import load_settings
from rag.loader import load_pdfs, split_documents
from rag.vectorstore import build_faiss_index, save_faiss_index


def main() -> None:
    settings = load_settings()
    docs = load_pdfs(settings)
    if not docs:
        print(f"No PDFs found in {settings.pdf_dir}. Please add files and retry.")
        return
    chunks = split_documents(settings, docs)
    vs = build_faiss_index(settings, chunks)
    save_faiss_index(vs, settings.vectorstore_dir)
    print(f"FAISS index saved to {settings.vectorstore_dir}")


if __name__ == "__main__":
    main()


