from flask import Flask, render_template, request

from workflows.optimization_graph import graph
from services.batch_optimizer import process_query_logs

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    opportunities = process_query_logs()

    if request.method == "POST":

        query = request.form["query"]

        result = graph.invoke(
            {
                "query": query,
                "runtime": 90,
                "cost": 50,
                "retry_count": 0,
                "logs": []
            }
        )

    return render_template(
        "index.html",
        result=result,
        opportunities=opportunities
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )