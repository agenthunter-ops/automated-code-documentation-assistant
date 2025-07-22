import os, uuid, asyncio, git
from pymongo import ReturnDocument
from src.core.config import settings
from src.core.database import db


async def clone_or_pull(url: str, branch: str = "main") -> str:
    repo_name = url.split("/")[-1].removesuffix(".git")
    local_path = os.path.join(settings.DEFAULT_CLONE_PATH, f"{repo_name}_{uuid.uuid4().hex[:6]}")
    os.makedirs(settings.DEFAULT_CLONE_PATH, exist_ok=True)

    if not os.path.exists(local_path):
        git.Repo.clone_from(url, local_path, branch=branch)
    else:
        repo = git.Repo(local_path)
        repo.remotes.origin.pull()

    # record / update repo in DB
    doc = await db.repos.find_one_and_update(
        {"url": url},
        {"$set": {"path": local_path, "branch": branch}},
        upsert=True,
        return_document=ReturnDocument.AFTER,
    )
    return str(doc["_id"])


async def latest_commit_sha(repo_path: str) -> str:
    repo = git.Repo(repo_path)
    return repo.head.commit.hexsha[:8]


async def monitor_repo(repo_id: str) -> None:
    repo_doc = await db.repos.find_one({"_id": repo_id})
    if not repo_doc:
        return
    old_sha = repo_doc.get("latest_sha")
    new_sha = await latest_commit_sha(repo_doc["path"])
    if new_sha != old_sha:
        await db.repos.update_one({"_id": repo_id}, {"$set": {"latest_sha": new_sha}})
        await db.changes.insert_one({"repo_id": repo_id, "old": old_sha, "new": new_sha})
