from app.group.model import Group
from app.dao.base import BaseDAO
from app.database import async_session_maker
from sqlalchemy import select
from sqlalchemy.orm import selectinload, joinedload


class GroupDAO(BaseDAO):
    model = Group

    @classmethod
    async def find_users_in_group(cls, **kwargs):
        async with async_session_maker() as session:
            query = select(cls.model).options(joinedload(cls.model.users)).filter_by(**kwargs)
            result = await session.execute(query)
            return result.unique().scalars().all()

    @classmethod
    async def find_shootings_in_group(cls, **kwargs):
        async with async_session_maker() as session:
            query = select(cls.model).options(joinedload(cls.model.shootings)).filter_by(**kwargs)
            result = await session.execute(query)
            return result.unique().scalars().all()