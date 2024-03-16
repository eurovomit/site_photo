from fastapi import APIRouter
from app.news.dao import NewsDAO
from app.news.schemas import SNews


router = APIRouter(prefix='/news', tags=['новости'])


@router.get('/ins')
async def ins_news():
    await NewsDAO.insert_data(name='Съёмка в ДС 1', description='23.04.24 состоится съемка в ДС № 1')
    await NewsDAO.insert_data(name='Съёмка в ДС 2', description='24.04.24 состоится съемка в ДС № 2')

