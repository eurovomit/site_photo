from fastapi import APIRouter
from app.payment.dao import PaymentDAO
from app.payment.schemas import SPayment


router = APIRouter(prefix='/payments', tags=['способы оплаты'])


@router.get('/ins')
async def ins_town():
    await PaymentDAO.insert_data(name='СБП')
    await PaymentDAO.insert_data(name='Банковская карта')

