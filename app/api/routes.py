# app/api/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import EnergyData
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

# DB oturumu
def get_db_session():
    db = next(get_db())
    try:
        yield db
    finally:
        db.close()

# Pydantic şemalar
class EnergyDataCreate(BaseModel):
    value: float
    timestamp: datetime | None = None

class EnergyPrediction(BaseModel):
    prediction: float | None
    message: str | None = None

# GET tüm veriler
@router.get("/energy")
def get_energy_data(db: Session = Depends(get_db)):
    return db.query(EnergyData).order_by(EnergyData.timestamp.desc()).all()

# POST yeni veri
@router.post("/energy")
def create_energy_data(data: EnergyDataCreate, db: Session = Depends(get_db)):
    db_data = EnergyData(value=data.value, timestamp=data.timestamp or datetime.utcnow())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

# GET id ile veri
@router.get("/energy/{id}")
def get_energy_by_id(id: int, db: Session = Depends(get_db)):
    data = db.query(EnergyData).filter(EnergyData.id == id).first()
    if not data:
        raise HTTPException(status_code=404, detail="Data not found")
    return data

# GET predict
@router.get("/predict", response_model=EnergyPrediction)
def predict_energy(db: Session = Depends(get_db)):
    data = db.query(EnergyData).order_by(EnergyData.timestamp.desc()).limit(5).all()
    if not data:
        return {"prediction": None, "message": "No data yet"}
    prediction = sum([d.value for d in data]) / len(data)  # basit ortalama
    return {"prediction": prediction, "message": "Prediction based on last 5 records"}
