from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Type(Base):
    __tablename__ = "type"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
