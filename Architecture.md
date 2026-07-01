### Core Project: Intelligent SQL Interpreter
The flagship project in this repository is an AI-driven analytics engine. It enables users to query structured data using natural language by retrieving relevant database schema fragments and generating SQL for local execution.

Key Philosophy: Local-first processing using Ollama for LLMs and embeddings, ensuring data privacy and reducing cloud costs 
Primary Tech Stack: Streamlit (Frontend), DuckDB (SQL Engine), ChromaDB (Vector Store), and Ollama (LLM/Embeddings) 

### Standalone ML Notebooks
The other_notebooks/ directory contains experimental implementations for various machine learning domains:
Clickbait Detection: NLP-based classification of news headlines.
Song Genre Classification: Acoustic feature analysis using PCA and classic classifiers.
Trash Image Classification: A Convolutional Neural Network (CNN) for waste management.
System Architecture

The following diagram illustrates how the Natural Language Space (User Questions) interacts with the Code Entity Space (Processing Scripts and Storage) within the SQL Interpreter project.

Diagram 1: End-to-End Query Lifecycle
<img width="2302" height="1570" alt="Image 01-07-2026 at 10 48" src="https://github.com/user-attachments/assets/8441e442-8a4e-4654-be4e-551219e26d6a" />

1. Code Entity Space
2. Natural Language Space
3. Input
4. Calls
5. Retrieves Schema
6. Generates SQL
7. Executes
8. DataFrame
9. Charts
10. User Question (Text)
11. app.py (Streamlit UI)
12. rag_pipeline.py (Schema Retrieval)
13. sql_generator.py (LLM Prompting)
14. DuckDB (ecommerce.duckdb)
15. visualization.py (Plotly)
16. Data and Metadata Flow
The system bridges the gap between raw data files and vectorized semantic search. The following diagram shows how the initialization scripts transform the Olist dataset into queryable entities.
