import datetime
from typing import Annotated

from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class News(Base):
    __tablename__ = "news"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]]
