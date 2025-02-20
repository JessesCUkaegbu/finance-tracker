from sqlalchemy.orm import Session
from app import models, schemas
from sqlalchemy import func
from passlib.hash import bcrypt


# User CRUD
def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = bcrypt.hash(user.password)
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get all user by their ID
def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


# Transaction CRUD
def create_transaction(db: Session, transaction: schemas.TransactionCreate, user_id: int):
    db_transaction = models.Transaction(**transaction.dict(), user_id=user_id)
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def get_transactions(db: Session, user_id: int):
    return db.query(models.Transaction).filter(models.Transaction.user_id == user_id).all()


# Create Budget
def create_budget(db: Session, budget: schemas.BudgetCreate, user_id: int):
    db_budget = models.Budget(**budget.dict(), user_id=user_id)
    db.add(db_budget)
    db.commit()
    db.refresh(db_budget)
    return db_budget

# Get all budgets for a user
def get_budgets(db: Session, user_id: int):
    return db.query(models.Budget).filter(models.Budget.user_id == user_id).all()

# Get a single budget by ID
def get_budget(db: Session, budget_id: int):
    return db.query(models.Budget).filter(models.Budget.id == budget_id).first()

# Update a budget
def update_budget(db: Session, budget_id: int, budget_data: schemas.BudgetCreate):
    db_budget = db.query(models.Budget).filter(models.Budget.id == budget_id).first()
    if db_budget:
        db_budget.category = budget_data.category
        db_budget.amount = budget_data.amount
        db.commit()
        db.refresh(db_budget)
    return db_budget

# Delete a budget
def delete_budget(db: Session, budget_id: int):
    db_budget = db.query(models.Budget).filter(models.Budget.id == budget_id).first()
    if db_budget:
        db.delete(db_budget)
        db.commit()
    return db_budget

# Calculation of financial income and expend for report and anaylsis.
def get_financial_report(db: Session, user_id: int, month: int = None, year: int = None):
    query = db.query(models.Transaction).filter(models.Transaction.user_id == user_id)

    if month and year:
        query = query.filter(func.extract('month', models.Transaction.date) == month)
        query = query.filter(func.extract('year', models.Transaction.date) == year)

    transactions = query.all()

    total_income = sum(t.amount for t in transactions if t.type == "income")
    total_expenses = sum(t.amount for t in transactions if t.type == "expense")
    balance = total_income - total_expenses

    return {
        "total_income": total_income,
        "total_expenses": total_expenses,
        "balance": balance,
        "transactions_count": len(transactions),
    }