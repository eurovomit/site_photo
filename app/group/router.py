from fastapi import APIRouter
from app.group.dao import GroupDAO
from app.group.schemas import SGroup


router = APIRouter(prefix='/groups', tags=['группы детских садов'])


@router.get('/ins')
async def ins_group():
    await GroupDAO.insert_data(name='старшая', kindergarten_id=18)
    await GroupDAO.insert_data(name='младшая', kindergarten_id=18)
    await GroupDAO.insert_data(name='ясли', kindergarten_id=18)
    await GroupDAO.insert_data(name='старшая', kindergarten_id=19)
    await GroupDAO.insert_data(name='младшая', kindergarten_id=19)
    await GroupDAO.insert_data(name='старшая', kindergarten_id=20)
    await GroupDAO.insert_data(name='младшая', kindergarten_id=20)
    await GroupDAO.insert_data(name='ясли', kindergarten_id=20)
    await GroupDAO.insert_data(name='старшая', kindergarten_id=21)
    await GroupDAO.insert_data(name='младшая', kindergarten_id=21)
    await GroupDAO.insert_data(name='ясли', kindergarten_id=21)
    await GroupDAO.insert_data(name='старшая', kindergarten_id=22)
    await GroupDAO.insert_data(name='младшая', kindergarten_id=22)
    await GroupDAO.insert_data(name='старшая', kindergarten_id=23)
    await GroupDAO.insert_data(name='младшая', kindergarten_id=23)
    await GroupDAO.insert_data(name='ясли', kindergarten_id=23)
    await GroupDAO.insert_data(name='старшая', kindergarten_id=24)
    await GroupDAO.insert_data(name='младшая', kindergarten_id=24)
    await GroupDAO.insert_data(name='старшая', kindergarten_id=25)
    await GroupDAO.insert_data(name='младшая', kindergarten_id=25)
    await GroupDAO.insert_data(name='ясли', kindergarten_id=25)

