from motor.motor_asyncio import AsyncIOMotorClient
from src.core.config import settings

client = AsyncIOMotorClient(settings.MONGODB_URL)
db = client["acda"]


async def init_indexes() -> None:
    await db.repos.create_index("url", unique=True)
    await db.docs.create_index([("repo_id", 1), ("path", 1)], unique=True)
