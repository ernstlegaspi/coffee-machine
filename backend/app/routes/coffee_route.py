from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.controller import coffee_controller
from app.database import SessionLocal
from app.schemas import MakeCoffee, Out, StatusOut, UpdateContainer

router = APIRouter(prefix="/api/coffee", tags=["coffee"])

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@router.post("/")
def make_coffee_machine(db: Session = Depends(get_db)):
  coffee_controller.make_coffee_machine(db)

  return { "message": "Coffee Machine Built!" }

@router.patch("/")
def make_coffee(data: MakeCoffee, db: Session = Depends(get_db)):
  coffee = coffee_controller.make_coffee(db, data)

  return { "message": f"Your {data.type} is ready!" }

@router.patch("/{coffee_machine_id}/refill-coffee", response_model=Out)
def refill_coffee(coffee_machine_id: int, db: Session = Depends(get_db)):
  coffee_machine = coffee_controller.refill_coffee(db, coffee_machine_id)

  return { "message": "Coffee successfully refilled to maximum capacity." }

@router.patch("/{coffee_machine_id}/refill-water", response_model=Out)
def refill_water(coffee_machine_id: int, db: Session = Depends(get_db)):
  coffee_machine = coffee_controller.refill_water(db, coffee_machine_id)

  return { "message": "Water successfully refilled to maximum capacity." }

@router.get("/{coffee_machine_id}/status", response_model=StatusOut)
def get_status(coffee_machine_id: int, db: Session = Depends(get_db)):
  coffee = coffee_controller.get_status(db, coffee_machine_id)

  return {
    "coffee_amount": coffee.coffee_amount,
    "water_amount": coffee.water_amount,
  }

@router.get("/")
def get_coffee_machine(db: Session = Depends(get_db)):
  return coffee_controller.get_coffee_machine(db)
