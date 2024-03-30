from fastapi import APIRouter

from app.kindergarten.schemas import SKindergarten
from app.town.dao import TownDAO
from app.town.schemas import STownPost


router = APIRouter(prefix='/towns', tags=['города'])

@router.get('')
async def get_towns_all() -> list[STownPost]:
    return await TownDAO.find_all()


@router.post('/ins')
async def ins_town(towns: list[STownPost]):
    lst = []
    for town in towns:
        await TownDAO.insert_data(name=town.name)
        lst.append(town.name)
    return f'добавлены города {lst}'


@router.get("/kgs")
async def select_kgs_in_town(town_id):
    return await TownDAO.find_kgs_in_town(id=int(town_id))