from fastapi import APIRouter
from app.basket.dao import BasketDAO
from app.basket.schemas import SBasket


router = APIRouter(prefix='/baskets', tags=['корзины'])


@router.get('/ins')
async def ins_basket():
    await BasketDAO.insert_data(content='[{"21": [{"15x22": 2},{"20x30": 1}]}, {"31": [{"10x15": 4}, {"calendar": 1}, {"magnet": 2}]}]', user_id=11)
    await BasketDAO.insert_data(content='[{"22": [{"15x22": 1}, {"20x30": 2}]}, {"32": [{"10x15": 3}, {"calendar": 1}, {"magnet": 4}]}]', user_id=12)

