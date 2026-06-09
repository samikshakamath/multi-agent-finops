from workflows.optimization_graph import graph
import json

result = graph.invoke(
    {
        "query": """
        SELECT *
        FROM sales
        WHERE YEAR(order_date)=2025
        """,
        "retry_count": 0
    }
)

print(json.dumps(result, indent=4))