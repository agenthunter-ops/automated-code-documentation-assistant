"""
Global pytest fixtures for ACDA tests.
Spins up a temporary in-memory MongoDB server (mongomock) and injects it
into the application so unit-tests never touch a real database.
"""
import asyncio
import os
import pytest
from motor.motor_asyncio import AsyncIOMotorClient
from mongomock_motor import AsyncMongoMockClient

from src.core import config as cfg_module
from src.core import database as db_module


@pytest.fixture(scope="session", autouse=True)
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session", autouse=True)
def patch_db(monkeypatch):
    # Substitute the AsyncIOMotorClient with an in-memory mongomock client
    client = AsyncMongoMockClient()
    db = client["acda_test"]

    monkeypatch.setattr(db_module, "client", client)
    monkeypatch.setattr(db_module, "db", db)

    # Disable telemetry / external calls when testing
    monkeypatch.setattr(cfg_module.settings, "OPENAI_API_KEY", "fake-key")
    monkeypatch.setattr(cfg_module.settings, "SLACK_BOT_TOKEN", None)
    monkeypatch.setattr(cfg_module.settings, "SLACK_CHANNEL_ID", None)

    yield
