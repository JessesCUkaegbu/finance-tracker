from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    
    
    transactions = relationship("Transaction", back_populates="user")
    

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    amount = Column(Float)
    type = Column(String)  # 'income' or 'expense'
    description = Column(String, nullable=True)  
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)


    user = relationship("User", back_populates="transactions")