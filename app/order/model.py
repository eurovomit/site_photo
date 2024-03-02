from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, JSON, Date


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    user_id = Column(ForeignKey("user.id"))
    content = Column(JSON)