from pydantic import BaseModel


class SKindergarten(BaseModel):
    id: int
    name: str
    town: str

    class Config:
        orm_mode = True