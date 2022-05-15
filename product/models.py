from sqlalchemy import *
from config.database import Base

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True)
    description = Column(String(255))
    price = Column(Float)
    quantity = Column(Integer)
    def __str__(self) -> str:
        return f"{self.name}"