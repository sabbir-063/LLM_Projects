## RAG_BookQA

Production-ready RAG pipeline for English/Bangla book Q&A using Gemini (Pro), FAISS, and LangChain. Includes:

- PDF ingestion and chunking
- FAISS vector store
- CLI infinite Q/A loop
- FastAPI service

### 1) Project layout

```
RAG_BookQA/
  app/
    __init__.py
    main.py
  data/
    pdfs/              # Put your Bangla/English PDFs here
    vectorstore/       # Auto-generated FAISS index here
  rag/
    __init__.py
    chain.py
    config.py
    embeddings.py
    llm.py
    loader.py
    retriever.py
    utils.py
    vectorstore.py
  scripts/
    __init__.py
    ingest_pdfs.py
    qa_cli.py
  .env.example
  requirements.txt
  README.md
```

### 2) Prerequisites

- Python 3.10+
- A valid Google Generative AI API key with access to Gemini Pro models

### 3) Setup

1. Copy your PDFs into `data/pdfs/`.
2. Create `.env` from the example and set your key/model:

```
cp .env.example .env
# Edit .env and set GOOGLE_API_KEY
```

3. Create a virtual environment and install dependencies:

```
python -m venv .venv
source .venv/bin/activate   # Windows (Git Bash): source .venv/Scripts/activate
pip install -U pip
pip install -r requirements.txt
```

### 4) Build vector index (ingestion)

```
python -m scripts.ingest_pdfs
```

This reads all PDFs in `data/pdfs/`, chunks content, embeds with Google embeddings, and writes a FAISS index to `data/vectorstore/`.

### 5) Run CLI Q/A (infinite loop)

```
python -m scripts.qa_cli
```

Type your question in English or Bangla. Type `exit` or `quit` to stop.

### 6) Run FastAPI service

```
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Example request:

```
curl -X POST "http://localhost:8000/ask" \
  -H "Content-Type: application/json" \
  -d '{"question": "Summarize chapter 1", "language": "auto"}'
```

Response includes the `answer` and `sources` (top retrieved chunks with file/page).

### 7) Notes

- `GEMINI_MODEL_NAME` defaults to `gemini-2.5-pro`. If your account uses a different identifier, set it in `.env`.
- `EMBEDDING_MODEL_NAME` defaults to `text-embedding-004`.
- You can tune chunk sizes, overlap, `k` retrieval, and temperature in `.env`.


