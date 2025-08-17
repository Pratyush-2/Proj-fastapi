from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# ---------- Food ----------
class Food(Base):
    __tablename__ = "foods"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    barcode = Column(String, nullable=True)
    calories = Column(Float)
    protein = Column(Float)
    carbs = Column(Float)
    fats = Column(Float)

    logs = relationship("DailyLog", back_populates="food")


# ---------- Daily Log ----------
class DailyLog(Base):
    __tablename__ = "daily_logs"

    id = Column(Integer, primary_key=True, index=True)
    food_id = Column(Integer, ForeignKey("foods.id"))
    quantity = Column(Float)   # grams or units
    date = Column(Date)

    food = relationship("Food", back_populates="logs")


# ---------- User Goal ----------
class UserGoal(Base):
    __tablename__ = "user_goals"

    id = Column(Integer, primary_key=True, index=True)
    calories_goal = Column(Float)
    protein_goal = Column(Float)
    carbs_goal = Column(Float)
    fats_goal = Column(Float)
