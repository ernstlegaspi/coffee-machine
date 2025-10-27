from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models import CoffeeMachine

RECIPES = {
  "espresso": { "coffee_g": 8, "water_ml": 24 },
  "double_espresso": { "coffee_g": 16, "water_ml": 48 },
  "americano": { "coffee_g": 16, "water_ml": 148 }
}

COFFEE_AMOUNT = 500
WATER_AMOUNT = 2000

FLAVORS = ["espresso", "double_espresso", "americano"]

def get_machine(db: Session, id: int):
  return db.query(CoffeeMachine).filter(CoffeeMachine.id == id).first()

def make_coffee_machine(db: Session):
  new_coffee_machine = CoffeeMachine()

  db.add(new_coffee_machine)
  db.commit()
  db.refresh(new_coffee_machine)

  return new_coffee_machine

def make_coffee(db: Session, data):
  coffee_machine = get_machine(db, data.coffee_machine_id)

  if not coffee_machine:
    raise HTTPException(status_code=404, detail="Coffee Machine not found!")

  if data.type not in FLAVORS:
    raise HTTPException(status_code=400, detail="Not available in our menu.")

  coffee_g = RECIPES[data.type]["coffee_g"]
  water_ml = RECIPES[data.type]["water_ml"]

  if coffee_machine.coffee_amount < coffee_g:
    raise HTTPException(status_code=400, detail="Not enough coffee. Please tell the staff to refill the coffee container.")

  if coffee_machine.water_amount < water_ml:
    raise HTTPException(status_code=400, detail="Not enough water. Please tell the staff to refill the water container.")

  coffee_machine.coffee_amount -= coffee_g
  coffee_machine.water_amount -= water_ml

  if data.type == "espresso":
    coffee_machine.espresso_count += 1
  elif data.type == "double_espresso":
    coffee_machine.double_espresso_count += 1
  elif data.type == "americano":
    coffee_machine.americano_count += 1
  else:
    raise HTTPException(status_code=400, detail="Your order is not on the menu!")

  db.commit()
  db.refresh(coffee_machine)

  return coffee_machine

def refill_coffee(db: Session, coffee_machine_id: int):
  coffee_machine = get_machine(db, coffee_machine_id)

  if not coffee_machine:
    raise HTTPException(status_code=404, detail="Coffee Machine not found!")

  if coffee_machine.coffee_amount > 300:
    raise HTTPException(status_code=400, detail="Coffee container has enough coffee, let our staff rest.")

  coffee_amount_to_be_add = COFFEE_AMOUNT - coffee_machine.coffee_amount
  coffee_machine.coffee_amount += coffee_amount_to_be_add

  db.commit()
  db.refresh(coffee_machine)

  return coffee_machine

def refill_water(db: Session, coffee_machine_id: int):
  coffee_machine = get_machine(db, coffee_machine_id)

  if not coffee_machine:
    raise HTTPException(status_code=404, detail="Coffee Machine not found!")

  if coffee_machine.water_amount > 1500:
    raise HTTPException(status_code=400, detail="Water container has enough water, let our staff rest.")

  water_amount_to_be_add = WATER_AMOUNT - coffee_machine.water_amount
  coffee_machine.water_amount += water_amount_to_be_add

  db.commit()
  db.refresh(coffee_machine)

  return coffee_machine

def get_status(db: Session, coffee_machine_id: int):
  coffee_machine = get_machine(db, coffee_machine_id)

  if not coffee_machine:
    raise HTTPException(status_code=404, detail="Coffee Machine not found!")

  return coffee_machine

def get_coffee_machine(db: Session):
  return db.query(CoffeeMachine).all()
