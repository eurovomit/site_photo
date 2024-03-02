from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Photo(Base):
    __tablename__ = "photo"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    path = Column(String, nullable=False)
    shooting_id = Column(ForeignKey("shooting.id"))