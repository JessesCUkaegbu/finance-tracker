from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from typing import List

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

# Budget Schemas
class BudgetBase(BaseModel):
    category: str
    amount: float

class BudgetCreate(BudgetBase):
    pass

class Budget(BudgetBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True 

class FinancialReportResponse(BaseModel):
    total_income: float
    total_expenses: float
    balance: float
    transactions_count: int

class Notification(BaseModel):
    message: str

class NotificationsResponse(BaseModel):
    notifications: List[Notification]