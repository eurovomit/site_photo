from fastapi import APIRouter
from app.town.dao import TownDAO
from app.town.schemas import STown


router = APIRouter(prefix='/towns', tags=['города'])

@router.get('')
async def get_towns_all() -> list[STown]:
    return await TownDAO.find_all()


@router.get('/ins')
async def ins_town():
    await TownDAO.insert_data(name='Калининград')
    await TownDAO.insert_data(name='Светлогорск')
    await TownDAO.insert_data(name='Балтийск')
    await TownDAO.insert_data(name='Советск')
