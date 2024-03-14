from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Theme(Base):
    __tablename__ = "theme"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    shootings: Mapped[list['Shooting']] = relationship(back_populates="theme")
