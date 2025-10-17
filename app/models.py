from sqlalchemy import Column, Integer, String
from .database import Base

class Rider(Base):
    __tablename__ = "riders"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True,nullable=False)
    latitude = Column(String, nullable=False)
    longitude = Column(String, nullable=False)