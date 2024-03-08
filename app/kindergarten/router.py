from fastapi import APIRouter
from app.kindergarten.dao import KindergartenDAO
from app.kindergarten.schemas import SKindergarten


router = APIRouter(prefix='/kindergartens', tags=['детские сады'])

@router.get('')
async def get_kg_all() -> list[SKindergarten]:
    return await KindergartenDAO.find_all()


@router.get('/test')
async def get_test() -> list[SKindergarten]:
    return await KindergartenDAO.find_one_or_none(town='Балтийск', name='2')


@router.get('/{town_id}')
async def get_kg_for_town(town_id) -> SKindergarten:
    return await KindergartenDAO.find_by_id(int(town_id))
