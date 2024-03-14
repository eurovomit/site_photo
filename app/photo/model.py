from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from sqlalchemy import ForeignKey


class Photo(Base):
    __tablename__ = "photo"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    path: Mapped[str] = mapped_column(nullable=False)
    shooting_id: Mapped[int] = mapped_column(ForeignKey("shooting.id", ondelete="CASCADE"))

    shooting: Mapped["Shooting"] = relationship(back_populates="photos")