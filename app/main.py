from typing import Union
from fastapi import FastAPI
from .database import engine
from . import models
from app.routers import users, transactions, budgets, reports
import uvicorn
from app.auth import auth


# Create Table
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(auth.router)


# Include Routers
app.include_router(users.router, prefix="/api")
app.include_router(transactions.router, prefix="/api")
app.include_router(budgets.router) 
app.include_router(reports.router) 

@app.get("/")
def read_root():
    return {"Message": "Welcome to the Pesonal Finance Tracker FastAPI"}



if __name__ == "__main__":
    try:
        uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
    except KeyboardInterrupt:
        print("Server shutting down gracefully...")