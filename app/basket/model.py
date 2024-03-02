from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, JSON


class Basket(Base):
    __tablename__ = "basket"

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("user.id"))
    content = Column(JSON)
