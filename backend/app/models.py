from sqlalchemy import Column, Integer, String, text

from app.database import Base

class CoffeeMachine(Base):
  __tablename__ = "CoffeeMachine"

  id = Column(Integer, primary_key=True, index=True)

  espresso_count = Column(Integer, nullable=True, default=0, server_default=text("0"))
  double_espresso_count = Column(Integer, nullable=True, default=0, server_default=text("0"))
  americano_count = Column(Integer, nullable=True, default=0, server_default=text("0"))
  coffee_amount = Column(Integer, nullable=True, default=500, server_default=text("500"))
  water_amount = Column(Integer, nullable=True, default=2000, server_default=text("2000"))
