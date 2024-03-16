from fastapi import APIRouter
from app.photo.dao import PhotoDAO
from app.photo.schemas import SPhoto


router = APIRouter(prefix='/photos', tags=['фотографии'])


@router.get('/ins')
async def ins_photo():
    await PhotoDAO.insert_data(name='12345.jpg', path='app/src/12345.jpg', shooting_id=42)
    await PhotoDAO.insert_data(name='12346.jpg', path='app/src/12346.jpg', shooting_id=42)
    await PhotoDAO.insert_data(name='12347.jpg', path='app/src/12347.jpg', shooting_id=42)
    await PhotoDAO.insert_data(name='12348.jpg', path='app/src/12348.jpg', shooting_id=42)
    await PhotoDAO.insert_data(name='12349.jpg', path='app/src/12349.jpg', shooting_id=42)
    await PhotoDAO.insert_data(name='12350.jpg', path='app/src/12350.jpg', shooting_id=42)
    await PhotoDAO.insert_data(name='12351.jpg', path='app/src/12351.jpg', shooting_id=42)
    await PhotoDAO.insert_data(name='12352.jpg', path='app/src/12352.jpg', shooting_id=42)
    await PhotoDAO.insert_data(name='12353.jpg', path='app/src/12353.jpg', shooting_id=42)
    await PhotoDAO.insert_data(name='12354.jpg', path='app/src/12354.jpg', shooting_id=42)
    await PhotoDAO.insert_data(name='12355.jpg', path='app/src/12355.jpg', shooting_id=42)
    await PhotoDAO.insert_data(name='12356.jpg', path='app/src/12356.jpg', shooting_id=42)
    await PhotoDAO.insert_data(name='12357.jpg', path='app/src/12357.jpg', shooting_id=42)

