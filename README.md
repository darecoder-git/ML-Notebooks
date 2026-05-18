# Intelligent SQL Interpreter
Natural Language Analytics using RAG, DuckDB, Streamlit, ChromaDB, and Local LLMs.

<img width="2240" height="1260" alt="Screenshot 2026-05-18 at 4 40 09 AM" src="https://github.com/user-attachments/assets/c2eb01ee-c7d3-4cbb-a592-d1a82aabd2d5" />

## Overview
Intelligent SQL Interpreter is a local-first AI analytics system that converts natural language business questions into executable SQL queries using Retrieval-Augmented Generation (RAG) over database schema metadata.
Instead of sending entire database schemas into an LLM prompt, the system retrieves only the most relevant tables and columns using semantic search. This dramatically improves SQL quality, scalability, latency, and token efficiency.
The generated SQL executes locally using DuckDB and results are visualized through an interactive Streamlit interface.
This project demonstrates a production-style architecture for scalable text-to-SQL systems.
# Features
Natural language → SQL generation
Semantic schema retrieval using ChromaDB
Local embeddings using Ollama
DuckDB analytical execution engine
Streamlit interactive UI
Automatic Plotly visualizations
CSV export
Local-first architecture
No cloud database required
Works on standard laptops
# Architecture
User Question
    ↓
Schema Embedding Retrieval (RAG)
    ↓
Relevant Tables & Columns
    ↓
LLM SQL Generation
    ↓
DuckDB Query Execution
    ↓
Pandas DataFrame
    ↓
Streamlit + Plotly Visualization
# Tech Stack
Component	Technology
Frontend	Streamlit
SQL Engine	DuckDB
Vector Database	ChromaDB
Embeddings	Ollama
LLM Interface	OpenAI-compatible API
Visualization	Plotly
Dataset	Kaggle Olist E-commerce
Language	Python


# Why This Project Matters
Most text-to-SQL demos fail at scale because they attempt to expose the entire warehouse schema to the LLM.
This project solves that problem by applying RAG to structured metadata rather than documents.
Instead of sending thousands of columns into the prompt, the system retrieves only the schema fragments relevant to the user's question.

# Benefits:
Lower token usage
Faster responses
Better SQL accuracy
Reduced hallucinations
Scalable architecture

# Dataset
This project uses the public Kaggle dataset:
Brazilian E-Commerce Public Dataset by Olist
The dataset contains:
orders
products
customers
payments
sellers
reviews
shipping information
Perfect for demonstrating:
aggregations
joins
trend analysis
customer analytics
revenue analysis
operational metrics


# Project Structure
intelligent-sql-interpreter/
├── app.py
├── load_data.py
├── build_embeddings.py
├── rag_pipeline.py
├── sql_generator.py
├── visualization.py
├── prompts.py
├── requirements.txt
├── data/
│   └── raw/
├── chroma_db/
└── ecommerce.duckdb

# Installation
1. Clone Repository
git clone <your_repo_url>
cd intelligent-sql-interpreter
2. Install Python Dependencies
pip install -r requirements.txt
3. Install Ollama
Install Ollama from:
Ollama Official Website
4. Pull Required Models

   
## Embedding Model
ollama pull nomic-embed-text

## LLM Model
ollama pull llama3

## Download Dataset
Download the Kaggle Olist dataset and place CSV files inside:
/data/raw/
Required CSVs:
olist_orders_dataset.csv
olist_order_items_dataset.csv
olist_order_payments_dataset.csv
olist_products_dataset.csv
olist_customers_dataset.csv
olist_sellers_dataset.csv

## Load Data into DuckDB

## Run:
python load_data.py
This creates:
ecommerce.duckdb
with all required tables loaded.

## Build Schema Embeddings
Run:
python build_embeddings.py
This step:
extracts schema metadata
generates embeddings
stores vectors inside ChromaDB

## Start Ollama
Run:
ollama serve
Launch Streamlit App
Run:
streamlit run app.py
The app opens in your browser.

## Example Questions
Try asking:
What are the top selling product categories?
Show monthly revenue trend.
Which sellers generated highest sales?
What payment method is most common?
Which states have highest order volume?
What is the average order value?
Show revenue trend by month.
Which products receive worst reviews?

## Example Workflow
User Input
What was our monthly revenue trend in 2018?
Retrieved Schema
orders.order_purchase_timestamp
order_payments.payment_value
order_id

## Generated SQL
SELECT
    DATE_TRUNC('month', order_purchase_timestamp) AS month,
    SUM(payment_value) AS revenue
FROM orders
JOIN order_payments USING(order_id)
GROUP BY 1
ORDER BY 1;

## Output
Interactive line chart
Data table
Downloadable CSV
RAG over Schema Metadata
This project applies Retrieval-Augmented Generation (RAG) to structured database metadata.
Instead of retrieving documents, the system retrieves:
table names
column names
datatypes
business context
This allows the LLM to generate more accurate SQL while keeping prompts compact and relevant.
Current V1 Scope

## Included:
Natural language querying
Semantic schema retrieval
SQL generation
DuckDB execution
Streamlit frontend
Plotly charts

## Not included yet:
SQL validation layer
Query permissions
Retry logic
Query optimization
Role-based access
Future Improvements
Planned V2 enhancements:
SQL safety validation
Read-only enforcement
Hallucination detection
Join relationship graphs
SQL explanation engine
Query retry agents
Multi-database connectors
Snowflake support
Redshift support
dbt metadata ingestion
Semantic caching
Authentication
Conversational memory
Performance
Expected runtime on standard laptops:
Stage	Expected Time
Schema retrieval	<2 sec
SQL generation	5–10 sec
DuckDB execution	1–5 sec
Visualization	<2 sec
## 
Typical end-to-end response time:
15–30 seconds
