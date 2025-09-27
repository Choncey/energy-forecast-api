from app.database import SessionLocal, Base, engine
from app.models import EnergyData
import datetime, random

Base.metadata.create_all(bind=engine)
db = SessionLocal()

for _ in range(10):
    db.add(EnergyData(timestamp=datetime.datetime.utcnow(), value=random.uniform(100, 500)))

db.commit()
db.close()
print("Dummy data inserted!")
