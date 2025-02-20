from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, database
from app . schemas import FinancialReportResponse
from typing import Optional

router = APIRouter(prefix="/reports", tags=["Reports & Analytics"])

@router.get("/financial-summary/{user_id}", response_model=FinancialReportResponse)
def get_financial_summary(
    user_id: int,
    month: Optional[int] = None,
    year: Optional[int] = None,
    db: Session = Depends(database.get_db)
):
    return crud.get_financial_report(db, user_id, month, year)
