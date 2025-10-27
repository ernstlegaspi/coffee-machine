from pydantic import BaseModel

class MakeCoffee(BaseModel):
  coffee_machine_id: int
  type: str

class UpdateContainer(BaseModel):
  amount: int

class StatusOut(BaseModel):
  coffee_amount: int
  water_amount: int

class Out(BaseModel):
  message: str
