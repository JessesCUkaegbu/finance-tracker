from typing import Union
from fastapi import FastAPI
from .database import engine
from . import models
from app.routers import users, transactions

from app.auth import auth


# Create Table
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(auth.router)


# Include Routers
app.include_router(users.router, prefix="/api")
app.include_router(transactions.router, prefix="/api")

@app.get("/")
def read_root():
    return {"Message": "Welcome to the Pesonal Finance Tracker FastAPI"}