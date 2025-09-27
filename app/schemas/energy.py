from pydantic import BaseModel
from datetime import date

class EnergyCreate(BaseModel):
    date: date
    consumption_kwh: float

class EnergyRead(EnergyCreate):
    id: int
    class Config:
        orm_mode = True
