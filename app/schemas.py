from typing import List, Optional

from pydantic import BaseModel


class FibBase(BaseModel):
    fib_number: int


class Fib(FibBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True