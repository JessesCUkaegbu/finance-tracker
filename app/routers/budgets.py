from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas, database

router = APIRouter(prefix="/budgets", tags=["Budgets"])

# Dependency to get database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Budget
@router.post("/", response_model=schemas.Budget)
def create_budget(budget: schemas.BudgetCreate, db: Session = Depends(get_db), user_id: int = 1):
    return crud.create_budget(db=db, budget=budget, user_id=user_id)

# Get all Budgets
@router.get("/", response_model=list[schemas.Budget])
def get_budgets(db: Session = Depends(get_db), user_id: int = 1):
    return crud.get_budgets(db=db, user_id=user_id)

# Get Budget by ID
@router.get("/{budget_id}", response_model=schemas.Budget)
def get_budget(budget_id: int, db: Session = Depends(get_db)):
    budget = crud.get_budget(db=db, budget_id=budget_id)
    if budget is None:
        raise HTTPException(status_code=404, detail="Budget not found")
    return budget

# Update Budget
@router.put("/{budget_id}", response_model=schemas.Budget)
def update_budget(budget_id: int, budget: schemas.BudgetCreate, db: Session = Depends(get_db)):
    updated_budget = crud.update_budget(db=db, budget_id=budget_id, budget_data=budget)
    if updated_budget is None:
        raise HTTPException(status_code=404, detail="Budget not found")
    return updated_budget

# Delete Budget
@router.delete("/{budget_id}")
def delete_budget(budget_id: int, db: Session = Depends(get_db)):
    deleted_budget = crud.delete_budget(db=db, budget_id=budget_id)
    if deleted_budget is None:
        raise HTTPException(status_code=404, detail="Budget not found")
    return {"message": "Budget deleted successfully"}
