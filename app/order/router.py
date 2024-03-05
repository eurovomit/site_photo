from fastapi import APIRouter
from app.database import async_session_maker
from sqlalchemy import select
from app.order.model import Order


router = APIRouter(prefix='/orders', tags=['заказы'])

@router.get('')
async def get_orders_all():
    async with async_session_maker() as session:
        query = select(Order)
        result = await session.execute(query)
        # return result.scalars().all()
        return result.mappings().all()


@router.get('/{user_id}')
def get_order_for_user(user_id):
    pass