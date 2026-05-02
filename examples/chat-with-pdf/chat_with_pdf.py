"""
Example: Chat with PDF
-----------------------
Upload a PDF, ask questions about it.
Uses RAG: PDF → chunks → ChromaDB → Claude

Usage:
    pip install anthropic chromadb pypdf
    python chat_with_pdf.py --pdf your_file.pdf
"""

import sys
import argparse
import hashlib
from pathlib import Path

import chromadb
from chromadb.utils import embedding_functions
from anthropic import Anthropic

# Try importing pypdf
try:
    from pypdf import PdfReader
except ImportError:
    print("Install pypdf: pip install pypdf")
    sys.exit(1)


# --- Setup ---
client = Anthropic()
chroma = chromadb.Client()
embedder = embedding_functions.DefaultEmbeddingFunction()
collection = chroma.get_or_create_collection("pdf_chat", embedding_function=embedder)


def extract_text(pdf_path: str) -> str:
    """Extract all text from a PDF file."""
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    """Split text into overlapping chunks."""
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i : i + chunk_size])
        if chunk:
            chunks.append(chunk)
    return chunks


def ingest_pdf(pdf_path: str):
    """Chunk and embed a PDF into ChromaDB."""
    print(f"📄 Reading {pdf_path}...")
    text = extract_text(pdf_path)
    chunks = chunk_text(text)

    ids = [hashlib.md5(c.encode()).hexdigest() for c in chunks]
    collection.add(documents=chunks, ids=ids)
    print(f"✅ Ingested {len(chunks)} chunks from PDF")


def ask(question: str, history: list[dict]) -> str:
    """RAG query: retrieve context + ask Claude."""
    results = collection.query(query_texts=[question], n_results=4)
    context = "\n\n---\n\n".join(results["documents"][0])

    system = f"""You are a helpful assistant that answers questions about a PDF document.
Use ONLY the context below to answer. If unsure, say so.

CONTEXT FROM PDF:
{context}"""

    history.append({"role": "user", "content": question})

    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        system=system,
        messages=history,
    )

    answer = response.content[0].text
    history.append({"role": "assistant", "content": answer})
    return answer


def main():
    parser = argparse.ArgumentParser(description="Chat with a PDF using Claude")
    parser.add_argument("--pdf", required=True, help="Path to PDF file")
    args = parser.parse_args()

    if not Path(args.pdf).exists():
        print(f"❌ File not found: {args.pdf}")
        sys.exit(1)

    ingest_pdf(args.pdf)

    print("\n💬 Chat with your PDF (type 'quit' to exit)\n")
    history = []

    while True:
        question = input("You: ").strip()
        if question.lower() in ("quit", "exit", "q"):
            break
        if not question:
            continue

        answer = ask(question, history)
        print(f"\n🤖 Claude: {answer}\n")


if __name__ == "__main__":
    main()
