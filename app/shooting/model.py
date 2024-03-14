import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from sqlalchemy import ForeignKey


class Shooting(Base):
    __tablename__ = "shooting"

    id: Mapped[int] = mapped_column(primary_key=True)
    theme_id: Mapped[int] = mapped_column(ForeignKey("theme.id", ondelete="CASCADE"))
    group_id: Mapped[int] = mapped_column(ForeignKey("group.id", ondelete="CASCADE"))
    date: Mapped[datetime.date] = mapped_column(nullable=False)

    theme: Mapped["Theme"] = relationship(back_populates="shootings")
    groups: Mapped[list['Group']] = relationship(back_populates="shootings", secondary="groupshooting")
    photos: Mapped[list["Photo"]] = relationship(back_populates="shooting")