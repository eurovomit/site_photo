from app.database import async_session_maker
from sqlalchemy import select
from app.kindergarten.model import Kindergarten
from app.dao.base import BaseDAO


class KindergartenDAO(BaseDAO):
    model = Kindergarten