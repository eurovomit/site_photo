from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Group(Base):
    __tablename__ = "group"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    kindergarten_id = Column(ForeignKey("kindergarten.id"))