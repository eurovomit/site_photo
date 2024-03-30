from app.kindergarten.model import Kindergarten
from app.dao.base import BaseDAO
from app.database import async_session_maker
from sqlalchemy import select
from sqlalchemy.orm import selectinload

class KindergartenDAO(BaseDAO):
    model = Kindergarten

    @classmethod
    async def find_groups_in_kg(cls, **kwargs):
        async with async_session_maker() as session:
            query = select(cls.model).options(selectinload(cls.model.groups)).filter_by(**kwargs)
            result = await session.execute(query)
            return result.scalars().all()