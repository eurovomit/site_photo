from app.user.model import User
from app.dao.base import BaseDAO


class UserDAO(BaseDAO):
    model = User