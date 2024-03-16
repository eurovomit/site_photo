from pydantic import BaseModel


class SGroup(BaseModel):
    id: int
    name: str
    kindergarten_id: int

    class Config:
        orm_mode = True