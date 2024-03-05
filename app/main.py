from fastapi import FastAPI, Query
from datetime import date
from typing import Optional, Annotated

from pydantic import BaseModel
from app.kindergarten.router import router as router_kg
from app.order.router import router as router_order

app = FastAPI()
app.include_router(router_kg)
app.include_router(router_order)

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