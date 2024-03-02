from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Theme(Base):
    __tablename__ = "theme"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
