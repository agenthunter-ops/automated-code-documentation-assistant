# Detailed Component Walk-Through

## Ingress Layer

### FastAPI HTTP Endpoint

**Endpoints:**
- `POST /repositories`: Register a new repository for documentation monitoring.
- `POST /repositories/{id}/scan`: Manually trigger a scan for a specific repository.
- `GET /health`: Health check probe.

**Why FastAPI?**
- Asynchronous I/O using `uvicorn` for high performance.
- Automatic OpenAPI spec generation for easy API exploration and integration.
- Robust request validation with Pydantic.
- Suitable for handling high-throughput webhook and REST API calls in real-time.

### Router (`agent_router.py`)
- Centralizes request parsing and validation.
- Houses authentication and optional rate limiting hooks.
- Delegates workflow control to LangGraph as the orchestrator through an `AsyncRouter` pattern.

## Core Orchestration

### LangGraph Workflow Router
- Implements a state machine to manage documentation tasks.
- Receives repository events and determines which agent(s) to trigger based on changes detected in Redis (e.g., commit SHA differences).
- Emits human-readable execution traces to LangSmith for observability.

### Shared State Store (Redis)
- Stores high-frequency, small-sized data items:
  - Latest git commit SHA per repository.
  - Semaphore locks and back-off timers for coordinated agent work.
- Uses TTL (time-to-live) for ephemeral job flags, ensuring duplicate scans are prevented.

## Multi-Agent System

| Agent                  | Responsibilities                                                                                |
|------------------------|-------------------------------------------------------------------------------------------------|
| **Repository Monitor** | Clones or pulls the latest code from Git using GitPython; emits SHA checksums; updates MongoDB. |
| **Code Analyzer**      | Uses Tree-sitter for AST parsing to extract function/class names, docstring existence, dependencies; stores symbols in MongoDB. |
| **Doc Generator**      | Performs Retrieval-Augmented Generation (RAG): embeds code with OpenAI, queries FAISS, auto-generates and inserts docstrings via GPT-4o-mini. |
| **Notifier**           | Gathers job results, sends Slack/email alerts to developers, posts run summaries to LangSmith.   |

## Data Stores

| Store            | Purpose                 | Typical Size             |
|------------------|------------------------|--------------------------|
| `MongoDB.repos`  | Repository metadata    | Kilobytes                |
| `MongoDB.docs`   | Generated docstrings   | Megabytes                |
| `FAISS index`    | Code embeddings        | Up to 10M vectors (HNSW) |

> All databases are accessed asynchronously for optimal concurrency (`motor` for MongoDB, native async Redis client).

## Observability & Tracing

- **LangSmith** logs every agent execution, call chain, prompt, and token usage for traceability and debugging.
- **Prometheus Exporter** gathers system metrics:
  - API request latency
  - Documentation generation success/failure rates
  - Vector search query timings
- Visual dashboards and alerts are set up in Grafana, warning on service-level objective (SLO) breaches.

## DevOps & Deployment

- **Docker Compose** orchestrates the application stack, bringing up:
  - The main FastAPI application and worker agents
  - MongoDB service
  - Redis service
- **GitHub Actions** for CI/CD:
  - Runs code linting (`black`, `flake8`)
  - Executes automated tests (`pytest` with in-memory mongomock)
  - Builds multi-architecture containers
  - Pushes images to GitHub Container Registry
  - (Optional) Deploys to cloud platforms like AWS ECS, Azure Container Apps, or Google Cloud Run

## Sequence of Events: Workflow Trace

1. **Push Event:** A code push triggers a GitHub webhook to the `/repositories/{id}/scan` endpoint.
2. **Router:** Receives the event and queues a `RepoScan` message.
3. **Workflow Orchestration (LangGraph):**
   - Checks Redis to compare the new commit SHA with the previously stored SHA.
   - If new, initiates the Repository Monitor Agent.
4. **Repository Monitor Agent:** Clones or pulls the latest repository contents; updates latest SHA in the store.
5. **Code Analyzer Agent:** Uses AST to update the symbol map; flags out-of-date or missing docstrings.
6. **Doc Generator Agent:** Queries the FAISS vector store for similar code contexts; invokes GPT-4o-mini for docstring generation; commits changes (as patch or PR comment).
7. **Notifier Agent:** Summarizes and sends notifications (e.g., Slack, email), and posts run link to LangSmith.
8. **Logging & Metrics:** LangSmith captures execution artifacts; Prometheus metrics are updated for monitoring.

With these coordinated components, the system provides end-to-end, agentic AI-powered code documentation management, covering everything from code monitoring to automated doc generation and team notification in a scalable, observable, and extensible architecture.