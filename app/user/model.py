from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from sqlalchemy import ForeignKey


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column()
    phone: Mapped[str] = mapped_column(nullable=False)
    group_id: Mapped[int] = mapped_column(ForeignKey("group.id", ondelete="CASCADE"))

    groups: Mapped[list['User']] = relationship(back_populates="users", secondary="groupuser")
    basket: Mapped["Basket"] = relationship(back_populates="user")
    orders: Mapped[list["Order"]] = relationship(back_populates="user")