from openai import OpenAI
from RAG.SQL_INTERPRETER.prompts import SQL_PROMPT
from RAG.SQL_INTERPRETER.rag_pipeline import retrieve_schema

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

MODEL_NAME = "llama3"


def generate_sql(question):

    schema = retrieve_schema(question)

    prompt = SQL_PROMPT.format(
        schema=schema,
        question=question
    )


    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0,
        top_p=0.1
    )



    import re
    sql = response.choices[0].message.content.strip()
    # remove markdown
    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")

    # # extract first SELECT query
    # match = re.search(
    #     r"(SELECT[\\s\\S]*?;)",
    #     sql,
    #     re.IGNORECASE
    # )

    # if match:
    #     sql = match.group(1)

    # sql = sql.strip()
    return sql









# Analytics Engineer with MCP + RAG systems exp — open to Snapmint's Business Analyst role
# Hi Swathi,

# I came across the Product Analyst role at Snapmint and wanted to reach out directly.

# I'm currently an Analytics Engineer at Pine Labs where I've built production systems including an MCP-based natural language to SQL engine over Redshift using RAG and ChromaDB — reducing ticket resolution time by 75%.
# My stack: Python, LangChain, LangGraph, RAG pipelines, AI Agents, Redshift, Streamlit, SQL.

# I have advanced proficiency in SQL, working knowledge of Python, and experience in building dashboards.

# Happy to share more if there's a fit. Would you have 15 minutes?

# Regards,
# Pravash Purkayastha
# 8920918893