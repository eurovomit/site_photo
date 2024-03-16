from app.basket.model import Basket
from app.dao.base import BaseDAO


class BasketDAO(BaseDAO):
    model = Basket