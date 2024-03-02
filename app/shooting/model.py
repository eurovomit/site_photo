from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date


class Shooting(Base):
    __tablename__ = "shooting"

    id = Column(Integer, primary_key=True)
    theme_id = Column(ForeignKey("theme.id"))
    group_id = Column(ForeignKey("group.id"))
    date = Column(Date, nullable=False)