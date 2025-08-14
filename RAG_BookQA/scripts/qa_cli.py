from __future__ import annotations

from rag.chain import ask_question, build_conversational_chain
from rag.config import load_settings
from rag.utils import format_sources, is_exit
from rag.vectorstore import load_faiss_index


def main() -> None:
    settings = load_settings()
    vs = load_faiss_index(settings)
    chain = build_conversational_chain(settings, vs)
    print("RAG CLI ready. Ask questions in English or Bangla. Type 'exit' to quit.")
    while True:
        try:
            question = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break
        if not question:
            continue
        if is_exit(question):
            print("Goodbye!")
            break
        answer, sources = ask_question(chain, question)
        print(f"\nAssistant: {answer}\n")
        if sources:
            print("Sources:\n" + format_sources(sources) + "\n")


if __name__ == "__main__":
    main()


