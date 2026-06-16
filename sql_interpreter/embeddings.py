import duckdb
import chromadb
import ollama

conn = duckdb.connect("ecommerce.duckdb")

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(name="schema_metadata")

schema_info = conn.execute("""
SELECT
    table_name,
    column_name,
    data_type
FROM information_schema.columns
WHERE table_schema = 'main'
""").fetchall()



for idx, row in enumerate(schema_info):
    table_name, column_name, data_type = row

    text = f"""
    Table: {table_name}
    Column: {column_name}
    Type: {data_type}
    """

    embedding = ollama.embeddings(
        model="nomic-embed-text",
        prompt=text
    )["embedding"]

    collection.add(
        ids=[str(idx)],
        documents=[text],
        embeddings=[embedding],
        metadatas=[{
            "table": table_name,
            "column": column_name
        }]
    )

print("Embeddings created successfully")