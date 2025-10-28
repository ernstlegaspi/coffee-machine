# migrations/env.py
from logging.config import fileConfig
import os

from sqlalchemy import engine_from_config, pool, create_engine
from alembic import context

config = context.config

# Force URL from env, default to docker-compose DSN
database_url = os.getenv("DATABASE_URL", "postgresql://fastapi_user:fastapi_pass@db:5432/fastapi_db")
config.set_main_option("sqlalchemy.url", database_url)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Import your metadata so autogenerate works
from app.database import Base
from app import models  # noqa: F401  (register tables)
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    url = database_url  # use our env URL directly
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    # Build engine directly from database_url to avoid ini placeholder issues
    connectable = create_engine(database_url, poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
