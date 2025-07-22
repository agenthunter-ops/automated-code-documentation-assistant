"""
Lightweight Slack utility used by notifier.py.
"""

import httpx
from src.core.config import settings

SLACK_API = "https://slack.com/api/chat.postMessage"


async def send(text: str) -> None:
    if not (settings.SLACK_BOT_TOKEN and settings.SLACK_CHANNEL_ID):
        return  # Slack not configured

    payload = {"channel": settings.SLACK_CHANNEL_ID, "text": text}
    headers = {
        "Authorization": f"Bearer {settings.SLACK_BOT_TOKEN}",
        "Content-Type": "application/json",
    }
    async with httpx.AsyncClient(timeout=10) as client:
        resp = await client.post(SLACK_API, json=payload, headers=headers)
        resp.raise_for_status()
