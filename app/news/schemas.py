import datetime

from pydantic import BaseModel


class SNews(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime.datetime

    class Config:
        orm_mode = True