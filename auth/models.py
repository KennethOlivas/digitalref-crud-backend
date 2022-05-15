from sqlalchemy import *
from config.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(255))
    def __str__(self) -> str:
        return f"{self.username}"