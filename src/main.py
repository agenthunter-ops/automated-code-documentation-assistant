from fastapi import FastAPI, BackgroundTasks, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from src.core.config import settings
from src.routing import agent_router
from src.core.database import init_indexes

app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)
app.include_router(agent_router.router)


@app.on_event("startup")
async def startup() -> None:
    # Create indexes asynchronously
    await init_indexes()

    # Lazy-load any warming tasks
    BackgroundTasks().add_task(lambda: None)


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}
