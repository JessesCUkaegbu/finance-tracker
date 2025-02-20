from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# User Schemas
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

# Transaction Schemas
class TransactionCreate(BaseModel):
    title: str
    amount: float
    type: str
    description: str
    date: datetime  

class TransactionCreate(TransactionCreate):
    pass

class TransactionOut(TransactionCreate):
    id: int
    user_id: int

    class Config:
        orm_mode = True