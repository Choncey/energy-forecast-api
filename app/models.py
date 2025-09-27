from sqlalchemy import Column, Integer, Float, DateTime
from app.database import Base
import datetime

class EnergyData(Base):
    __tablename__ = "energy_data"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    value = Column(Float)
