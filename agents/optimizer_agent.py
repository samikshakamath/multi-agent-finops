from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


def optimize_query(query: str):

    prompt = f"""
You are a Senior Database Performance Engineer.

Your task is to optimize SQL safely.

STRICT RULES:

1. Preserve business logic.
2. Never invent tables.
3. Never invent columns.
4. Never invent filters.
5. Never assume schema information.
6. If the query cannot be safely optimized,
   return the ORIGINAL query unchanged.
7. Only rewrite obvious anti-patterns such as:

   YEAR(date_column)=2025

   into

   date_column >= '2025-01-01'
   AND date_column < '2026-01-01'

8. Return ONLY SQL.
9. No markdown.
10. No explanations.

Query:

{query}
"""

    response = llm.invoke(prompt)

    return response.content.strip()