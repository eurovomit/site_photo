import datetime

from pydantic import BaseModel
from sqlalchemy import JSON


class SOrder(BaseModel):
    id: int
    # content: JSON
    created_at: datetime.datetime
    user_id: int

    class Config:
        orm_mode = True