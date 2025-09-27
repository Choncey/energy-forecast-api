from logging.config import fileConfig
from dotenv import load_dotenv
import os
import sys

from alembic import context

# -------------------------
# Proje dizinini path’e ekle
# -------------------------
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# -------------------------
# .env dosyasını yükle
# -------------------------
load_dotenv()

DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"

# Alembic Config object
config = context.config

# Logging ayarları
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# -------------------------
# Modeli import et ve target_metadata ayarla
# -------------------------
from app.models import Base  # Energy modelindeki Base
target_metadata = Base.metadata

# -------------------------
# Offline migration
# -------------------------
def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

# -------------------------
# Online migration
# -------------------------
def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    from sqlalchemy import create_engine
    connectable = create_engine(DATABASE_URL)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

# -------------------------
# Migration modunu seç
# -------------------------
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
