from fastapi import APIRouter
from app.user.dao import UserDAO
from app.user.schemas import SUser


router = APIRouter(prefix='/users', tags=['пользователи'])


@router.get('/ins')
async def ins_user():
    await UserDAO.insert_data(name='Вика', email='test1@test.com', password='123', phone='+79001234567', group_id=45)
    await UserDAO.insert_data(name='Женя', email='test2@test.com', password='123', phone='+79001234568', group_id=45)
    await UserDAO.insert_data(name='Маша', email='test3@test.com', password='123', phone='+79001234569', group_id=45)
    await UserDAO.insert_data(name='Лена', email='test4@test.com', password='123', phone='+79001234560', group_id=46)
    await UserDAO.insert_data(name='Алёна', email='test5@test.com', password='123', phone='+79001234561', group_id=46)

