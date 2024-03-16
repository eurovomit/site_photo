from fastapi import APIRouter
from app.type.dao import TypeDAO
from app.type.schemas import SType


router = APIRouter(prefix='/types', tags=['размеры фото'])


@router.get('/ins')
async def ins_type():
    await TypeDAO.insert_data(name='10x15', price=150)
    await TypeDAO.insert_data(name='15x22', price=250)
    await TypeDAO.insert_data(name='20x30', price=350)
    await TypeDAO.insert_data(name='30x40', price=500)
    await TypeDAO.insert_data(name='Календарь', price=500)
    await TypeDAO.insert_data(name='Магнит', price=100)

