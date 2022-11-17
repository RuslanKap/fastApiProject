from pathlib import Path

from fastapi import FastAPI, Depends, Request
from fastapi.staticfiles import StaticFiles
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from .db import async_session
from .models import Posts
from .service import get_post_by_text

BASE_DIR = Path(__file__).resolve().parent.parent


# Dependency
async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session


app = FastAPI()
templates = Jinja2Templates(directory=Path(BASE_DIR, "app/templates/"))
app.mount("/static", StaticFiles(directory=Path(BASE_DIR, "app/templates/")), name="static")


@app.get('/')
async def main(request: Request):
    if request.headers.get('HX-Request'):
        return templates.TemplateResponse('info.html', context={'request': request, 'flag': True})
    return templates.TemplateResponse('index.html', context={'request': request, 'flag': False})


@app.get('/search')
async def search_post(request: Request, search_text: str, db: AsyncSession = Depends(get_db)):
    if search_text == '':
        return RedirectResponse('/')
    vm = await get_post_by_text(search_text, db=db)
    if request.headers.get('HX-Request'):
        if vm:
            return templates.TemplateResponse("search_results.html", {"request": request, "posts": vm})
        else:
            return templates.TemplateResponse("search_results.html",
                                              {"request": request, "message": "нет информации по запросу"})
    return templates.TemplateResponse('index.html', {"request": request, "posts": vm, "search_text": search_text})


@app.get('/textsearch')
async def read_item(search: str, db: AsyncSession = Depends(get_db)):
    q = await get_post_by_text(search, db=db)
    if not q:
        return JSONResponse(status_code=404, content={'message': 'нет информации по запросу'})
    return q


@app.delete('/post/{id}')
async def delete_person(id: int, db: AsyncSession = Depends(get_db)):
    post = await db.get(Posts, id)
    if post is None:
        return JSONResponse(status_code=404, content={'message': f'Пост с id = {id} не найден'})
    await db.delete(post)
    await db.commit()
    return post
