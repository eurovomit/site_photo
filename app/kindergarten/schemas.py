from pydantic import BaseModel


class SKindergarten(BaseModel):
    id: int
    name: str
    town_id: int

    class Config:
        orm_mode = True