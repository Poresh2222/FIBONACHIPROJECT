from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from . database import Base


class Numbers(Base):
    __tablename__ = "Fibonacci_Numbers"

    id = Column(Integer, primary_key=True, index=True)
    fib_number = Column(Integer)
    is_active = Column(Boolean, default=True)