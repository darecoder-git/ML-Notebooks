import chromadb
import ollama

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_collection(name="schema_metadata")


def retrieve_schema(question, top_k=15):

    embedding = ollama.embeddings(
        model="nomic-embed-text",
        prompt=question
    )["embedding"]

    results = collection.query(
        query_embeddings=[embedding],
        n_results=top_k
    )

    documents = results["documents"][0]

    return "\n".join(documents)