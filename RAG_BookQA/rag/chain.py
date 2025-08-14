from __future__ import annotations

from typing import Dict, List, Tuple

from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate

from .config import RAGSettings
from .llm import create_llm
from .retriever import create_retriever


SYSTEM_PROMPT = (
    "You are a helpful research assistant for Q&A over books in English and Bangla. "
    "Answer in the same language as the user's question (English or Bangla). "
    "Use only the provided context. If the answer is not in the context, say you do not know."
)


def build_conversational_chain(settings: RAGSettings, vector_store: FAISS) -> ConversationalRetrievalChain:
    llm = create_llm(settings)
    retriever = create_retriever(settings, vector_store)

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key="answer",
    )

    # Chat prompt for combine docs phase: expects 'context' and 'question'
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", SYSTEM_PROMPT + "\n\nContext:\n{context}"),
            ("human", "{question}"),
        ]
    )

    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        verbose=False,
        chain_type="stuff",
        return_source_documents=True,
        combine_docs_chain_kwargs={"prompt": prompt},
    )

    return chain


def ask_question(chain: ConversationalRetrievalChain, question: str) -> Tuple[str, List[Dict]]:
    result = chain.invoke({"question": question})
    answer: str = result.get("answer", "")
    sources = []
    for doc in result.get("source_documents", []) or []:
        metadata = doc.metadata or {}
        sources.append(
            {
                "source": metadata.get("source"),
                "page": metadata.get("page"),
                "score": metadata.get("score"),
            }
        )
    return answer, sources


