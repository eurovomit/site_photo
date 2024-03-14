from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Town(Base):
    __tablename__ = "town"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()

    kindergartens: Mapped[list['Kindergarten']] = relationship(back_populates="town")
