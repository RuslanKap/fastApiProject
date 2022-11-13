import pytest
from httpx import AsyncClient
from app.main import app



@pytest.mark.asyncio
async def test_get_something() -> None:
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/textsearch?search=NODATA")
    assert response.status_code == 404
    assert response.text == '{"message":"нет информации по запросу"}'


@pytest.mark.asyncio
async def test_get_something() -> None:
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/textsearch?search=dd")
    assert response.status_code == 200
    assert 20 >= len(response.json()) > 0
