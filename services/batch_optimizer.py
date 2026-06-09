import pandas as pd

from workflows.optimization_graph import graph


def process_query_logs():

    df = pd.read_csv("data/query_logs.csv")

    results = []

    for _, row in df.iterrows():

        result = graph.invoke(
    {
        "query": row["query_text"],
        "runtime": row["execution_time"],
        "cost": row["cost"],
        "retry_count": 0,
        "logs": []
    }
)

        results.append(
            {
                "query_id": row["query_id"],
                "runtime": row["execution_time"],
                "cost": row["cost"],
                "issues": result["issues"],
                "optimized_query": result["optimized_query"],
                "estimated_savings": result["savings"]["estimated_cost_savings"]
            }
        )

    results.sort(
        key=lambda x: x["estimated_savings"],
        reverse=True
    )

    return results