from fastapi import FastAPI, Query
from datetime import date
from typing import Optional, Annotated

from pydantic import BaseModel
from app.kindergarten.router import router as router_kg
from app.order.router import router as router_order
from app.town.router import router as router_town
from app.group.router import router as router_group
from app.theme.router import router as router_theme
from app.shooting.router import router as router_shooting
from app.user.router import router as router_user
from app.photo.router import router as router_photo
from app.basket.router import router as router_basket
from app.order.router import router as router_order
from app.type.router import router as router_type
from app.payment.router import router as router_payment
from app.news.router import router as router_news

app = FastAPI()
app.include_router(router_kg)
app.include_router(router_order)
app.include_router(router_town)
app.include_router(router_group)
app.include_router(router_theme)
app.include_router(router_shooting)
app.include_router(router_user)
app.include_router(router_photo)
app.include_router(router_basket)
app.include_router(router_order)
app.include_router(router_type)
app.include_router(router_payment)
app.include_router(router_news)

@app.get("/")
async def get_news():
    return {"new": "съемка в ДС"}


class SPhoto(BaseModel):
    ds: int
    date: date
    is_vertical: bool | None
    count: int | None

@app.get("/photos/{ds}")
def get_photos(ds: int,
               date: date,
               is_vertical: Annotated[bool | None, Query()] = None,
               count: Annotated[int | None, Query(ge=1)] = None) -> list[SPhoto]:
    photos = [
        {
            "ds": ds,
            "date": date,
            "is_vertical": is_vertical,
            "count": count
        },
    ]
    return photos


class SOrder(BaseModel):
    photo_id: int
    size: str
    count: int

@app.post("/order")
def add_order(order: SOrder):
    pass