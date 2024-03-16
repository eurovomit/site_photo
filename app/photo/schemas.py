from pydantic import BaseModel


class SPhoto(BaseModel):
    id: int
    name: str
    path: str
    shooting_id: int

    class Config:
        orm_mode = True