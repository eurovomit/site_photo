from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from sqlalchemy import ForeignKey

from app.group.model import Group


class Kindergarten(Base):
    __tablename__ = "kindergarten"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    town_id: Mapped[int] = mapped_column(ForeignKey("town.id", ondelete="CASCADE"))

    town: Mapped["Town"] = relationship(back_populates="kindergartens")
    groups: Mapped[list[Group]] = relationship(back_populates="kindergarten")