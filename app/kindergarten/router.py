from fastapi import APIRouter
from app.kindergarten.dao import KindergartenDAO
from app.kindergarten.schemas import SKindergarten


router = APIRouter(prefix='/kindergartens', tags=['детские сады'])

@router.get('')
async def get_kg_all() -> list[SKindergarten]:
    return await KindergartenDAO.find_all()


# @router.get('/test')
# async def get_test() -> list[SKindergarten]:
#     return await KindergartenDAO.find_one_or_none(town='Балтийск', name='2')


# @router.get('/{town_id}')
# async def get_kg_for_town(town_id) -> SKindergarten:
#     return await KindergartenDAO.find_by_id(int(town_id))


@router.get('/ins')
async def ins_kg():
    await KindergartenDAO.insert_data(name='110', town_id=15)
    await KindergartenDAO.insert_data(name='111', town_id=15)
    await KindergartenDAO.insert_data(name='112', town_id=15)
    await KindergartenDAO.insert_data(name='Солнышко', town_id=16)
    await KindergartenDAO.insert_data(name='Аистёнок', town_id=16)
    await KindergartenDAO.insert_data(name='1', town_id=17)
    await KindergartenDAO.insert_data(name='2', town_id=17)
    await KindergartenDAO.insert_data(name='Чебурашка', town_id=18)
