from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, database

router = APIRouter(prefix="/notifications", tags=["Notifications"])

@router.get("/{user_id}")
def get_user_notifications(user_id: int, db: Session = Depends(database.get_db)):
    return crud.get_notifications(db, user_id)