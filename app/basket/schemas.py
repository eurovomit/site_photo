from pydantic import BaseModel
from sqlalchemy import JSON


class SBasket(BaseModel):
    id: int
    # content: JSON
    user_id: int

    class Config:
        orm_mode = True