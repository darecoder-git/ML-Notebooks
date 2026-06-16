import duckdb

conn = duckdb.connect("ecommerce.duckdb")


# /Users/purkayastha7/Desktop/Codes./SQL_INTERPRETER/data

files = {
    "orders": "./SQL_INTERPRETER/data/raw/olist_orders_dataset.csv",
    "order_items": "./SQL_INTERPRETER/data/raw/olist_order_items_dataset.csv",
    "order_payments": "./SQL_INTERPRETER/data/raw/olist_order_payments_dataset.csv",
    "products": "./SQL_INTERPRETER/data/raw/olist_products_dataset.csv",
    "customers": "./SQL_INTERPRETER/data/raw/olist_customers_dataset.csv",
    "sellers": "./SQL_INTERPRETER/data/raw/olist_sellers_dataset.csv"
}

for table_name, path in files.items():
    conn.execute(f"""
        CREATE OR REPLACE TABLE {table_name} AS
        SELECT *
        FROM read_csv_auto('{path}')
    """)

    print(f"Loaded {table_name}")

print("All tables loaded into DuckDB")