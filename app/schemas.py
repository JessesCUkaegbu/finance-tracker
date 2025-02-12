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
    amount: float
    description: Optional[str] = None

class TransactionOut(BaseModel):
    id: int
    amount: float
    description: Optional[str]
    date: datetime

    class Config:
        orm_mode = True
