from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from fib_fun import crud
from app import schemas
from SQL_app import models
from SQL_app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/generatefibnum/", response_model=schemas.Fib)
def create_fibnum(num: schemas.FibBase, db: Session = Depends(get_db)):
    return crud.create_fibnum(db=db, num=num)


@app.get("/fibnumdb/", response_model=List[schemas.Fib])
def read_fibnum(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    numbers = crud.get_fibnum(db, skip=skip, limit=limit)
    return numbers