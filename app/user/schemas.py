from pydantic import BaseModel


class SUser(BaseModel):
    id: int
    name: str
    email: str
    password: str
    phone: str
    group_id: int

    class Config:
        orm_mode = True