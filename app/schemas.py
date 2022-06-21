from datetime import date
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str
    address: str
    phone: str

    class Config:
        orm_mode = True
