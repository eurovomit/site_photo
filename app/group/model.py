from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from sqlalchemy import ForeignKey


class Group(Base):
    __tablename__ = "group"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    kindergarten_id: Mapped[int] = mapped_column(ForeignKey("kindergarten.id", ondelete="CASCADE"))

    kindergarten: Mapped["Kindergarten"] = relationship(back_populates="groups")
    shootings: Mapped[list['Shooting']] = relationship(back_populates="groups", secondary="groupshooting")
    users: Mapped[list['User']] = relationship(back_populates="groups", secondary="groupuser")


class GroupShooting(Base):
    __tablename__ = "groupshooting"

    group_id: Mapped[int] = mapped_column(ForeignKey("group.id", ondelete="CASCADE"), primary_key=True)
    shhoting_id: Mapped[int] = mapped_column(ForeignKey("shooting.id", ondelete="CASCADE"), primary_key=True)


class GroupUser(Base):
    __tablename__ = "groupuser"

    group_id: Mapped[int] = mapped_column(ForeignKey("group.id", ondelete="CASCADE"), primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"), primary_key=True)