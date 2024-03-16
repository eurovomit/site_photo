from datetime import datetime

from pydantic import BaseModel


class SShooting(BaseModel):
    id: int
    theme_id: int
    group_id: int
    # date: datetime.date

    class Config:
        orm_mode = True