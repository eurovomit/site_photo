from fastapi import APIRouter
from app.theme.dao import ThemeDAO
from app.theme.schemas import STheme


router = APIRouter(prefix='/themes', tags=['темы съемок'])


@router.get('/ins')
async def ins_theme():
    await ThemeDAO.insert_data(name='гусары')
    await ThemeDAO.insert_data(name='морозко')
    await ThemeDAO.insert_data(name='франция')
    await ThemeDAO.insert_data(name='машинка')

