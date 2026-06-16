import streamlit as st
import duckdb
import pandas as pd

from sql_generator import generate_sql
from visualization import render_chart

st.set_page_config(
    page_title="Intelligent SQL Interpreter",
    layout="wide"
)

st.title("Intelligent SQL Interpreter")

st.markdown(
    "Ask business questions in natural language"
)

question = st.text_input(
    "Ask a question",
    placeholder="What were the top selling categories in 2018?"
)

if question:

    with st.spinner("Generating SQL..."):
        sql = generate_sql(question)

    st.subheader("Generated SQL")
    st.code(sql, language="sql")

    conn = duckdb.connect("ecommerce.duckdb")

    try:
        df = conn.execute(sql).fetchdf()

        st.subheader("Results")
        st.dataframe(df)

        chart = render_chart(df)

        if chart:
            st.subheader("Visualization")
            st.plotly_chart(chart, use_container_width=True)

        csv = df.to_csv(index=False)

        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="results.csv",
            mime="text/csv"
        )

    except Exception as e:
        st.error(f"Query failed: {e}")
