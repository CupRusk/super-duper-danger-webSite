from sqlalchemy import Column, Integer, String
from logic.db.database import Base

class User(Base):
    __tablename__ = "User" # таблицы обычно во множественном числе

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, unique=True)
    login = Column(String(21), unique=True, index=True, nullable=False)
    password_hash = Column(String(124), nullable=False)
    password = Column(String(124), nullable=False)
    ip = Column(String(45), nullable=True)
    country = Column(String(100), nullable=True) 
