from pydantic import BaseModel


class STheme(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True