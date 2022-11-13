from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from .models import Posts


async def get_post_by_text(search_text: str, db: AsyncSession):
    # db.query(Posts).filter(Posts.text.ilike(f'%{search_text}%')).order_by(Posts.created_date.desc()).limit(20).all()
    result = await db.execute(
        select(Posts).filter(Posts.text.ilike(f'%{search_text}%')).order_by(Posts.created_date.desc()).limit(20))
    # result = await db.execute(
    #         select(Posts).filter("posts.text @@ to_tsquery(:search_text)").order_by(Posts.created_date.desc()).limit(20))
    return result.scalars().all()

# session.query(TableName).\
#     filter("t.column_name @@ to_tsquery(:search_string)").params(search_string=search_string).all()

#
# async def del_post(id: int, db: AsyncSession):
#     post = await db.execute(select(Posts).filter(Posts.id == id))
#     print(post)
#     # post = post.scalar_one()
#     print(post)
#     await db.delete(post)
#     await db.commit()
#     # return post
