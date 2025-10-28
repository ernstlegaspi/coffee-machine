# ☕ Coffee Machine Project

A simple FastAPI + Vue.js application to simulate a coffee machine.

## 🚀 Setup Instructions

Follow the steps below to run the project locally using Docker.

### 1. Clone the Repository
```bash
# Make an empty directory and open CMD
git clone https://github.com/ernstlegaspi/coffee-machine
```bash

2. Run the Frontend
# Open a new terminal for the frontend
cd ./frontend
docker compose up --build

3. Setup the Backend
# Open another terminal for the backend
cd ./backend
alembic init migrations

4. Configure Alembic
4.1. Open the file:
./backend/migrations/env.py

4.2. Copy the code from copy-env.py.

4.3. Paste it into env.py and modify it as needed.

5. Build and Run the Backend
docker compose up --build -d

6. Apply Database Migrations
# Create initial migration
docker-compose exec web alembic revision --autogenerate -m "init"

# Apply the migration
docker-compose exec web alembic upgrade head
