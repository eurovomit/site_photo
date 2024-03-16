from pydantic import BaseModel


class STown(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True