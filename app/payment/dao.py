from app.payment.model import Payment
from app.dao.base import BaseDAO


class PaymentDAO(BaseDAO):
    model = Payment
