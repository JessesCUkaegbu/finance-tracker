from typing import Union
from fastapi import FastAPI
from .database import engine
from . import models

from app.auth import auth


# Create Table
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"Message": "Welcome to the Pesonal Finance Tracker FastAPI"}