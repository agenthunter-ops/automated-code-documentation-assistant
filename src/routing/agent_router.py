from fastapi import APIRouter, HTTPException, BackgroundTasks, status
from pydantic import BaseModel, HttpUrl

from src.agents import repository_monitor, code_analyzer, doc_generator, notifier
from src.core.database import db

router = APIRouter(prefix="/repositories", tags=["repositories"])


class RepoIn(BaseModel):
    url: HttpUrl
    branch: str | None = "main"


@router.post("", status_code=status.HTTP_201_CREATED)
async def add_repo(repo: RepoIn, tasks: BackgroundTasks):
    repo_id = await repository_monitor.clone_or_pull(repo.url, repo.branch)
    tasks.add_task(notifier.slack_post, f"🎉 New repository registered: {repo.url}")
    return {"id": repo_id}


@router.post("/{repo_id}/scan")
async def scan_repo(repo_id: str, tasks: BackgroundTasks):
    repo_doc = await db.repos.find_one({"_id": repo_id})
    if not repo_doc:
        raise HTTPException(404, "Repository not found")

    tasks.add_task(repository_monitor.monitor_repo, repo_id)
    return {"msg": "Scan scheduled"}
