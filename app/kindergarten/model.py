from app.database import Base
from sqlalchemy import Column, Integer, String


class Kindergarten(Base):
    __tablename__ = "kindergarten"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    town = Column(String, nullable=False)