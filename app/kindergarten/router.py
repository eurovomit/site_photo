from fastapi import APIRouter
from app.kindergarten.dao import KindergartenDAO
from sqlalchemy import select
from app.kindergarten.model import Kindergarten


router = APIRouter(prefix='/kindergartens', tags=['детские сады'])

@router.get('')
async def get_kg_all():
    return await KindergartenDAO.find_all()


@router.get('/{town_id}')
def get_kg_for_town(town_id):
    pass
