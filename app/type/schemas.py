from pydantic import BaseModel


class SType(BaseModel):
    id: int
    name: str
    price: int

    class Config:
        orm_mode = True