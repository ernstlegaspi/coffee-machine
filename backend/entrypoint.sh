#!/bin/sh
# Wait a few seconds to ensure DB is ready (simple approach)
sleep 3

# Apply Alembic migrations
alembic upgrade head

# Start FastAPI
uvicorn app.main:app --host 0.0.0.0 --port 8000
