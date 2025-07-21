# Automated Code Documentation Assistant

**Automated, AI-powered code documentation that keeps your project’s docs up-to-date—powered by Agentic AI and multi-agent workflows.**

## 🚩 Problem Statement

Maintaining accurate, up-to-date code documentation is a constant challenge in software development. Manual documentation is often neglected, leading to confusion, inefficient onboarding, and poor code maintainability.  
This project uses Agentic AI to automate documentation—actively monitoring code repositories, detecting discrepancies, and assisting developers in closing documentation gaps.

## 🎯 Key Features

### Must-Have
- **Repository Monitoring**: Watches Git-based code repositories for changes.
- **Initial Documentation Generation**: Auto-generates documentation (e.g., README, API/module docs) on setup by analysing repo structure.
- **Code Change Detection**: Tracks new commits and code modifications.
- **Outdated or Missing Docs Detection**: Identifies docs that are out-of-sync or missing for new/modified features.
- **Notification System**: Alerts developers when docs need attention.

### Good to Have
- **Draft Documentation Generation**: Suggests doc snippets for new/updated code (using LLMs/RAG).
- **Documentation Suggestions**: Recommends areas to focus on.
- **Integration**: Supports platforms like Confluence or Read the Docs.
- **Custom Rules**: Lets teams define their own documentation heuristics.
- **Developer Feedback**: Improves by learning from user response.

## 👨‍💻 Technical Approach

- **Code Parsing & Understanding**: Language-agnostic AST parsing and relationship extraction.
- **Semantic Architecture Extraction**: Identifies boundaries, dependencies, and interactions in code.
- **Multi-Agent AI**: Specialised agents coordinate analysis and action.
- **Diagram Generation**: Optionally auto-generates code diagrams for clarity.
- **Notification/Alert System**: Developer-friendly alerts on documentation issues.

## 🔧 Tech Stack

- **LangChain, LangGraph**: Agentic workflow orchestration.
- **OpenAI GPT / RAG**: LLM-powered generation and reasoning.
- **Python, FastAPI, asyncio**: Backend and async processing.
- **MongoDB, FAISS**: Conversation, task, and vector storage.
- **Docker**: Containerized deployment.
- **LangSmith**: Observability and pipeline debugging.

## 🚀 Getting Started

1. **Clone this repo** and install dependencies.
2. **Configure connection** to your Git repository.
3. **Run agent services** (with Docker or locally).
4. **Trigger analysis** via new repository events or manually.
5. **Review docs & notifications** as new code is committed.

## ✅ How to Test

- Point the agent at a sample/public repo.
- Observe initial documentation generation.
- Make code changes to trigger detection.
- Check for alerts about outdated or missing docs.
- (If enabled) Review AI-generated documentation snippets.

## 📢 Stakeholders

- Software/dev teams, technical writers, onboarding managers, PMs—anyone who depends on accurate docs.

## 🤖 Solution Value

This project demonstrates the “Agentic AI” theme—automating real developer tasks and freeing teams to focus on building, not documenting.

## 📚 References

- See `/docs` for workflow diagrams and related research.

> _Hackathon project for automating, modernising, and futureproofing documentation in fast-moving codebases._
