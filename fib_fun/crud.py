from sqlalchemy.orm import Session

from app import main, schemas
from SQL_app import models, sql_main


def get_fibnum(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Numbers).offset(skip).limit(limit).all()


def create_fibnum(num: schemas.FibBase):
    
    fib1 = fib2 = 1

    fib3 = num.fib_number - 2

    while fib3 > 0:
        fib1, fib2 = fib2, fib1 + fib2
        fib3 -= 1
    return(fib2)

    sql_main.writte_in_db