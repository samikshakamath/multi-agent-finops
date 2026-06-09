def estimate_savings(
    old_runtime: float,
    new_runtime: float,
    old_cost: float
):

    runtime_reduction = (
        (old_runtime - new_runtime)
        / old_runtime
    ) * 100

    estimated_new_cost = (
        old_cost *
        (new_runtime / old_runtime)
    )

    cost_savings = (
        old_cost -
        estimated_new_cost
    )

    return {
        "runtime_reduction_pct":
            round(runtime_reduction, 2),

        "estimated_cost_savings":
            round(cost_savings, 2),

        "new_estimated_cost":
            round(estimated_new_cost, 2)
    }