from pydantic import BaseModel


class SPayment(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True