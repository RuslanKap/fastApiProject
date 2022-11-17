from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from .models import Posts


async def get_post_by_text(search_text: str, db: AsyncSession):

    result = await db.execute(
        select(Posts).filter(Posts.text.ilike(f'%{search_text}%')).order_by(Posts.created_date.desc()).limit(20))

    return result.scalars().all()

