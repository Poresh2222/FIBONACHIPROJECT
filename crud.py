from sqlalchemy.orm import Session

import models, schemas, main



def get_fibnum(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Numbers).offset(skip).limit(limit).all()


def create_fibnum(db: Session, num: schemas.FibBase):
    
    fib1 = fib2 = 1

    fib3 = num.fib_number - 2

    while fib3 > 0:
        fib1, fib2 = fib2, fib1 + fib2
        fib3 -= 1
 
    db_fibnumber = models.Numbers(fib_number=fib2)
    
    db.add(db_fibnumber)
    db.commit()
    db.refresh(db_fibnumber)
    return db_fibnumber