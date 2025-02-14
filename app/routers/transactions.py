from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud, database

router = APIRouter()

@router.post("/transactions/", response_model=schemas.TransactionOut)
def create_transaction(transaction: schemas.TransactionCreate, user_id: int, db: Session = Depends(database.get_db)):
    return crud.create_transaction(db, transaction, user_id)

@router.get("/transactions/{user_id}", response_model=list[schemas.TransactionOut])
def read_transactions(user_id: int, db: Session = Depends(database.get_db)):
    return crud.get_transactions(db, user_id)