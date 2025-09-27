from sqlalchemy.orm import Session
from app.models import Energy
from app.schemas.energy import EnergyCreate

# POST: yeni enerji kaydı ekle
def create_energy(db: Session, data: EnergyCreate):
    db_energy = Energy(date=data.date, consumption_kwh=data.consumption_kwh)
    db.add(db_energy)
    db.commit()
    db.refresh(db_energy)
    return db_energy

# GET: tüm enerji verilerini listele
def get_all_energy(db: Session):
    return db.query(Energy).all()
