from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "IP"

    ip = Column(Integer, primary_key=True, index=True)
    country = Column(String, primary_key=False)
