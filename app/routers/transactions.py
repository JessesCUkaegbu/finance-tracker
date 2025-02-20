from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, models, crud, database

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a transaction
@router.post("/transactions/", response_model=schemas.TransactionOut)
def create_transaction(transaction: schemas.TransactionCreate, user_id: int, db: Session = Depends(database.get_db)):
    return crud.create_transaction(db, transaction, user_id)

# Retrieve a single transaction by ID
@router.get("/transactions/{user_id}", response_model=list[schemas.TransactionOut])
def read_transactions(user_id: int, db: Session = Depends(database.get_db)):
    return crud.get_transactions(db, user_id)


# Update a transaction
@router.put("/{transaction_id}", response_model=schemas.TransactionOut)
def update_transaction(transaction_id: int, updated_data: schemas.TransactionCreate, db: Session = Depends(get_db)):
    transaction = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")

    for key, value in updated_data.dict().items():
        setattr(transaction, key, value)

    db.commit()
    db.refresh(transaction)
    return transaction

# Delete a transaction
@router.delete("/{transaction_id}")
def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):
    transaction = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")

    db.delete(transaction)
    db.commit()
    return {"message": "Transaction deleted successfully"}

