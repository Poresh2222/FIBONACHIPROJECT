from sqlalchemy.orm import Session

from fib_fun import crud
from app import main, schemas
from SQL_app import models


def writte_in_db(db: Session, num: schemas.FibBase):
    db_fibnumber = models.Numbers(fib_number=crud.create_fibnum(num=num))
    
    db.add(db_fibnumber)
    db.commit()
    db.refresh(db_fibnumber)
    
    return db_fibnumber