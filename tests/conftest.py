from typing import Generator
import pytest
from httpx import AsyncClient
from asyncio import get_event_loop

from app.main import app
from app.db import async_session


@pytest.fixture(scope="session")
def db() -> Generator:
    yield async_session()


@pytest.fixture(scope="module")
async def async_client() -> Generator:
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as client:
        yield client


@pytest.fixture(scope="module")
def event_loop():
    loop = get_event_loop()

    yield loop
