import datetime

from fastapi import APIRouter
from app.shooting.dao import ShootingDAO
from app.shooting.schemas import SShooting


router = APIRouter(prefix='/shootings', tags=['съемки'])


@router.get('/ins')
async def ins_shooting():
    await ShootingDAO.insert_data(theme_id=9, group_id=45, date=datetime.datetime.strptime('2024-02-24', '%Y-%m-%d'))
    await ShootingDAO.insert_data(theme_id=9, group_id=46, date=datetime.datetime.strptime('2024-02-24', '%Y-%m-%d'))
    await ShootingDAO.insert_data(theme_id=9, group_id=47, date=datetime.datetime.strptime('2024-02-24', '%Y-%m-%d'))
    await ShootingDAO.insert_data(theme_id=9, group_id=48, date=datetime.datetime.strptime('2024-02-25', '%Y-%m-%d'))
    await ShootingDAO.insert_data(theme_id=9, group_id=49, date=datetime.datetime.strptime('2024-02-25', '%Y-%m-%d'))
    await ShootingDAO.insert_data(theme_id=10, group_id=50, date=datetime.datetime.strptime('2024-02-26', '%Y-%m-%d'))
    await ShootingDAO.insert_data(theme_id=10, group_id=51, date=datetime.datetime.strptime('2024-02-26', '%Y-%m-%d'))
    await ShootingDAO.insert_data(theme_id=10, group_id=52, date=datetime.datetime.strptime('2024-02-27', '%Y-%m-%d'))
    await ShootingDAO.insert_data(theme_id=10, group_id=53, date=datetime.datetime.strptime('2024-02-28', '%Y-%m-%d'))
    await ShootingDAO.insert_data(theme_id=10, group_id=54, date=datetime.datetime.strptime('2024-02-28', '%Y-%m-%d'))
    await ShootingDAO.insert_data(theme_id=11, group_id=56, date=datetime.datetime.strptime('2024-02-29', '%Y-%m-%d'))
    await ShootingDAO.insert_data(theme_id=11, group_id=57, date=datetime.datetime.strptime('2024-02-29', '%Y-%m-%d'))
    await ShootingDAO.insert_data(theme_id=11, group_id=58, date=datetime.datetime.strptime('2024-03-01', '%Y-%m-%d'))
    await ShootingDAO.insert_data(theme_id=11, group_id=59, date=datetime.datetime.strptime('2024-03-01', '%Y-%m-%d'))
    await ShootingDAO.insert_data(theme_id=11, group_id=60, date=datetime.datetime.strptime('2024-03-01', '%Y-%m-%d'))
    await ShootingDAO.insert_data(theme_id=11, group_id=61, date=datetime.datetime.strptime('2024-03-02', '%Y-%m-%d'))
    await ShootingDAO.insert_data(theme_id=11, group_id=62, date=datetime.datetime.strptime('2024-03-02', '%Y-%m-%d'))
    await ShootingDAO.insert_data(theme_id=12, group_id=63, date=datetime.datetime.strptime('2024-03-03', '%Y-%m-%d'))
    await ShootingDAO.insert_data(theme_id=12, group_id=64, date=datetime.datetime.strptime('2024-03-03', '%Y-%m-%d'))
    await ShootingDAO.insert_data(theme_id=12, group_id=65, date=datetime.datetime.strptime('2024-03-03', '%Y-%m-%d'))

