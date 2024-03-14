import datetime
from typing import Annotated

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from sqlalchemy import Column, Integer, ForeignKey, JSON, text


class Order(Base):
    __tablename__ = "order"

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]]
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    content = Column(JSON)

    user: Mapped["User"] = relationship(back_populates="orders")