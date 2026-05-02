"""
Basic RAG (Retrieval Augmented Generation) Pattern
---------------------------------------------------
1. Chunk documents
2. Embed and store in vector DB
3. Retrieve relevant chunks on query
4. Pass to LLM with context
"""

import os
from anthropic import Anthropic
import chromadb
from chromadb.utils import embedding_functions

# --- Setup ---
client = Anthropic()
chroma = chromadb.Client()
embedder = embedding_functions.DefaultEmbeddingFunction()

collection = chroma.get_or_create_collection(
    name="knowledge_base",
    embedding_function=embedder,
)

# --- 1. Ingest Documents ---
def ingest(documents: list[str], ids: list[str]):
    """Add documents to the vector store."""
    collection.add(documents=documents, ids=ids)
    print(f"✅ Ingested {len(documents)} documents")


# --- 2. Retrieve ---
def retrieve(query: str, n_results: int = 3) -> list[str]:
    """Get top-k relevant chunks for a query."""
    results = collection.query(query_texts=[query], n_results=n_results)
    return results["documents"][0]


# --- 3. Generate ---
def rag_query(query: str) -> str:
    """Full RAG pipeline: retrieve + generate."""
    chunks = retrieve(query)
    context = "\n\n".join(chunks)

    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        system=f"""You are a helpful assistant. 
Answer questions using ONLY the context provided below.
If the answer isn't in the context, say "I don't have that information."

CONTEXT:
{context}""",
        messages=[{"role": "user", "content": query}],
    )
    return response.content[0].text


# --- Example Usage ---
if __name__ == "__main__":
    # Ingest some docs
    docs = [
        "FastAPI is a modern Python web framework for building APIs.",
        "LangChain is a framework for building LLM-powered applications.",
        "ChromaDB is an open-source vector database for AI applications.",
    ]
    ingest(docs, ids=["doc1", "doc2", "doc3"])

    # Query
    answer = rag_query("What is ChromaDB?")
    print(f"\n🤖 Answer: {answer}")
