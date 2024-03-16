from fastapi import APIRouter
from app.order.dao import OrderDAO
from app.order.schemas import SOrder


router = APIRouter(prefix='/orders', tags=['заказы'])


@router.get('/ins')
async def ins_basket():
    await OrderDAO.insert_data(content='[{"24": [{"15x22": 2}, {"20x30": 1}]}, {"27": [{"10x15": 4}, {"calendar": 1}, {"magnet": 2}]}]', user_id=13)
    await OrderDAO.insert_data(content='[{"25": [{"15x22": 2}, {"20x30": 1}]}, {"28": [{"10x15": 4}, {"calendar": 1}, {"magnet": 2}]}]', user_id=14)

