#!/bin/bash

# -----------------------------
# Energy Forecast API Setup
# -----------------------------

# 1️⃣ PostgreSQL server başlat
echo "Starting PostgreSQL server..."
/opt/homebrew/opt/postgresql@14/bin/pg_ctl -D /opt/homebrew/var/postgresql@14 -l /opt/homebrew/var/postgresql@14/logfile start

# 2️⃣ Sanal ortamı aktif et
echo "Activating virtual environment..."
source venv/bin/activate

# 3️⃣ Alembic migration çalıştır
echo "Running Alembic migrations..."
alembic upgrade head

# 4️⃣ Backend’i başlat (FastAPI örnek)
echo "Starting backend server..."
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000


