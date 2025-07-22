# REST API Reference

> Base URL: `/` (default `http://localhost:8000`)

| Method & Path | Description | Request Body | Response |
|---------------|-------------|--------------|----------|
| `GET /health` | Health probe | – | `{"status":"ok"}` |
| `POST /repositories` | Register & clone a Git repo | `{ "url": "...", "branch": "main" }` | `{ "id": "<repo_id>" }` |
| `POST /repositories/{id}/scan` | Schedule a scan for new commits | – | `{ "msg": "Scan scheduled" }` |

## Example: Register Repository

