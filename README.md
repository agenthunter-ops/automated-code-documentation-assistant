# Automated Code Documentation Assistant

**Automated, AI-powered code documentation that keeps your project’s docs up-to-date—powered by Agentic AI and multi-agent workflows.**

## 🚩 Problem Statement

Maintaining accurate, up-to-date code documentation is a constant challenge in software development. Manual documentation is often neglected, leading to confusion, inefficient onboarding, and poor code maintainability[1].  
This project uses Agentic AI to automate documentation—actively monitoring code repositories, detecting discrepancies, and assisting developers in closing documentation gaps[1].

## 🎯 Key Features

### Must-Have
- **Repository Monitoring**: Watches Git-based code repositories for changes[1].
- **Initial Documentation Generation**: Auto-generates documentation (e.g., README, API/module docs) on setup by analysing repo structure[1].
- **Code Change Detection**: Tracks new commits and code modifications[1].
- **Outdated or Missing Docs Detection**: Identifies docs that are out-of-sync or missing for new/modified features[1].
- **Notification System**: Alerts developers when docs need attention[1].

### Good to Have
- **Draft Documentation Generation**: Suggests doc snippets for new/updated code (using LLMs/RAG)[1].
- **Documentation Suggestions**: Recommends areas to focus on[1].
- **Integration**: Supports platforms like Confluence or Read the Docs[1].
- **Custom Rules**: Lets teams define their own documentation heuristics[1].
- **Developer Feedback**: Improves by learning from user response[1].

## 👨‍💻 Technical Approach

- **Code Parsing & Understanding**: Language-agnostic AST parsing and relationship extraction[1].
- **Semantic Architecture Extraction**: Identifies boundaries, dependencies, and interactions in code[1].
- **Multi-Agent AI**: Specialized agents coordinate analysis and action[1].
- **Diagram Generation**: Optionally auto-generates code diagrams for clarity[1].
- **Notification/Alert System**: Developer-friendly alerts on documentation issues[1].

## 🔧 Tech Stack

- **LangChain, LangGraph**: Agentic workflow orchestration[1].
- **OpenAI GPT / RAG**: LLM-powered generation and reasoning[1].
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
- (If enabled) Review AI-generated documentation snippets[1].

## 📢 Stakeholders

- Software/dev teams, technical writers, onboarding managers, PMs—anyone who depends on accurate docs[1].

## 🤖 Solution Value

This project demonstrates the “Agentic AI” theme—automating real developer tasks and freeing teams to focus on building, not documenting[1].

## 📚 References

- See `/docs` for workflow diagrams and related research[1].

> _Hackathon project for automating, modernising, and futureproofing documentation in fast-moving codebases._

[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/81660344/b4b7bf3b-5c81-4a21-b97e-d2879d24283f/AutomatedCode_Documentation_Assistant_v1.0.docx
