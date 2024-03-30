from pydantic import BaseModel

from app.kindergarten.model import Kindergarten


class STownPost(BaseModel):
    name: str

    class Config:
        orm_mode = True