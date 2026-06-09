from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import json

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

def profile_query(query: str):

    prompt = f"""
You are a SQL performance expert.

Analyze this SQL query.

Identify ONLY:
- full_table_scan
- select_star
- missing_filter
- inefficient_join

Return ONLY valid JSON.

Format:

{{
    "issues": []
}}

Query:
{query}
"""

    response = llm.invoke(prompt)

    try:
        return json.loads(response.content)
    except Exception:
        return {"issues": []}