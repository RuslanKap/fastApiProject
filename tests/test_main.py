import pytest
from httpx import AsyncClient
from sqlalchemy.orm import Session

from app.main import app
import warnings
from trio import TrioDeprecationWarning
warnings.filterwarnings(action='ignore', category=TrioDeprecationWarning)


@pytest.mark.anyio
async def test_search_post(async_client: AsyncClient, db: Session) ->  None:
    response = await async_client.get("/textsearch?search=test")
    assert response.status_code == 404
    # print(response.json())
    # assert response.text == '{"message":"нет информации по запросу"}'

    import pytest
    from httpx import AsyncClient
    from fastapi import status
    from sqlalchemy.orm import Session

    # @pytest.mark.asyncio
    # async def test_get_something(async_client: AsyncClient, db: Session) -> None:
    #     await create_something(db=db)
    #     response = await async_client.get("/something?skip=0&limit=5")
    #
    #     assert response.status_code == status.HTTP_200_OK
    #     assert 0 < len(response.json()) <= 5