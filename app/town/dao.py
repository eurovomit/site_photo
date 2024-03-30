from app.town.model import Town
from app.dao.base import BaseDAO
from app.database import async_session_maker
from sqlalchemy import select
from sqlalchemy.orm import selectinload


class TownDAO(BaseDAO):
    model = Town

    @classmethod
    async def find_kgs_in_town(cls, **kwargs):
        async with async_session_maker() as session:
            query = select(cls.model).options(selectinload(cls.model.kindergartens)).filter_by(**kwargs)
            result = await session.execute(query)
            return result.scalars().all()
