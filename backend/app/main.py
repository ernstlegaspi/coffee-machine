from fastapi import FastAPI

from app.routes import coffee_route

app = FastAPI()

app.include_router(coffee_route.router)
