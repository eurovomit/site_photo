from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String)
    phone = Column(String)
    group_id = Column(ForeignKey("group.id"))