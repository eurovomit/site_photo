from app.order.model import Order
from app.dao.base import BaseDAO


class OrderDAO(BaseDAO):
    model = Order