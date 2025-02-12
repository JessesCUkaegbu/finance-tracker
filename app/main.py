from typing import Union
from fastapi import FastAPI
from .database import engine
from . import models


# Create Table
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Message": "Welcome to the Pesonal Finance Tracker FastAPI"}