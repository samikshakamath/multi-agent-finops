# Autonomous Multi-Agent FinOps SQL Optimizer

A multi-agent AI system that analyzes SQL queries, detects performance issues, generates optimized SQL, validates the output, and estimates potential cloud cost savings.

Built using LangGraph, OpenAI, SQLGlot, Flask, Docker, and GitHub Actions.

## Overview

The goal of this project is to automate SQL optimization workflows that are typically performed manually by data engineers and FinOps teams.

Given a SQL query, the system:

* Detects inefficient query patterns
* Generates an optimized version
* Validates SQL safety and syntax
* Estimates runtime and cost savings
* Displays results through a Flask dashboard

## Architecture

```text
Query
  ↓
Profiler Agent
  ↓
Optimizer Agent
  ↓
Validator Agent
  ↓
FinOps Agent
  ↓
Dashboard
```

The workflow is orchestrated using LangGraph, where each agent updates a shared state object and passes control to the next step.

## Agents

### Profiler Agent

Uses an LLM to identify common SQL performance issues:

* Full table scans
* SELECT *
* Missing filters
* Inefficient joins

### Optimizer Agent

Generates optimized SQL while preserving the original business logic.

### Validator Agent

Uses SQLGlot to:

* Validate syntax
* Block unsafe operations
* Enforce read-only SQL

### FinOps Agent

Estimates:

* Runtime reduction
* Cost savings
* New projected query cost

## Example

Input:

```sql
SELECT *
FROM sales
WHERE YEAR(order_date)=2025
```

Output:

```sql
SELECT *
FROM sales
WHERE order_date >= '2025-01-01'
AND order_date < '2026-01-01'
```

## Tech Stack

* Python
* LangGraph
* OpenAI GPT-4o-mini
* SQLGlot
* Flask
* Pandas
* Docker
* Pytest
* GitHub Actions

## Features

* Multi-agent workflow orchestration
* SQL optimization
* Query validation
* FinOps cost estimation
* Batch query analysis
* Agent execution logs
* Dockerized deployment
* CI/CD with GitHub Actions

## Running Locally

```bash
pip install -r requirements.txt
python -m dashboard.app
```

## Running with Docker

```bash
docker build -t multi-agent-finops .
docker run -p 5000:5000 --env-file .env multi-agent-finops
```

## Future Improvements

* Databricks query history integration
* CrewAI-based agent collaboration
* AWS ECS deployment
* Advanced FinOps analytics

```
```
