from typing import TypedDict

from langgraph.graph import StateGraph, END

from agents.profiler_agent import profile_query
from agents.optimizer_agent import optimize_query
from agents.validator_agent import validate_query
from agents.finops_agent import estimate_savings


class GraphState(TypedDict):
    query: str
    runtime: float
    cost: float
    issues: list
    optimized_query: str
    optimization_status: str
    validation: dict
    savings: dict
    retry_count: int
    logs: list


def profiler_node(state):

    result = profile_query(
        state["query"]
    )

    state["issues"] = result["issues"]

    state["logs"].append(
        f"Profiler Agent → Found issues: {', '.join(result['issues'])}"
    )

    return state


def optimizer_node(state):

    optimized = optimize_query(
        state["query"]
    )

    state["optimized_query"] = optimized

    if optimized.strip() == state["query"].strip():

        state["optimization_status"] = (
            "No Safe Optimization Available"
        )

        state["logs"].append(
            "Optimizer Agent → No safe optimization available"
        )

    else:

        state["optimization_status"] = (
            "Optimized Successfully"
        )

        state["logs"].append(
            "Optimizer Agent → Generated optimized SQL"
        )

    return state


def validator_node(state):

    validation = validate_query(
        state["optimized_query"]
    )

    state["validation"] = validation

    state["logs"].append(
        f"Validator Agent → {validation['reason']}"
    )

    return state


def finops_node(state):

    old_runtime = state["runtime"]
    old_cost = state["cost"]

    if state["optimization_status"] == "Optimized Successfully":

        improvement_factor = 0.40

    else:

        improvement_factor = 0.0

    new_runtime = (
        old_runtime *
        (1 - improvement_factor)
    )

    state["savings"] = estimate_savings(
        old_runtime=old_runtime,
        new_runtime=new_runtime,
        old_cost=old_cost
    )

    state["logs"].append(
        f"FinOps Agent → Estimated savings ${state['savings']['estimated_cost_savings']}"
    )

    return state


def route_validation(state):

    if state["validation"]["valid"]:
        return "finops"

    if state.get("retry_count", 0) >= 2:
        return "finops"

    state["retry_count"] = (
        state.get("retry_count", 0) + 1
    )

    return "optimizer"


builder = StateGraph(GraphState)

builder.add_node(
    "profiler",
    profiler_node
)

builder.add_node(
    "optimizer",
    optimizer_node
)

builder.add_node(
    "validator",
    validator_node
)

builder.add_node(
    "finops",
    finops_node
)

builder.set_entry_point(
    "profiler"
)

builder.add_edge(
    "profiler",
    "optimizer"
)

builder.add_edge(
    "optimizer",
    "validator"
)

builder.add_conditional_edges(
    "validator",
    route_validation,
    {
        "optimizer": "optimizer",
        "finops": "finops"
    }
)

builder.add_edge(
    "finops",
    END
)

graph = builder.compile()