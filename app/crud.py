"""CRUD operations for the Nutrition API."""

from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas

# ---------- Food ----------
def create_food(db: Session, food: schemas.FoodCreate):
    """Create a new food item."""
    db_food = models.Food(**food.dict())
    db.add(db_food)
    db.commit()
    db.refresh(db_food)
    return db_food

def get_foods(db: Session, skip: int = 0, limit: int = 100):
    """Get all food items."""
    return db.query(models.Food).offset(skip).limit(limit).all()


# ---------- Daily Logs ----------
def create_daily_log(db: Session, log: schemas.DailyLogCreate):
    """Create a new daily log."""
    # Ensure the food exists before logging
    db_food = db.query(models.Food).filter(models.Food.id == log.food_id).first()
    if not db_food:
        raise HTTPException(status_code=400, detail="Food not found")

    db_log = models.DailyLog(**log.dict())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

def get_logs_by_date(db: Session, date):
    """Get all daily logs for a given date."""
    return db.query(models.DailyLog).filter(models.DailyLog.date == date).all()


# ---------- User Goals ----------
def set_goal(db: Session, goal: schemas.UserGoalCreate):
    """Set a new user goal."""
    db_goal = models.UserGoal(
        calories_goal=goal.calories_goal,
        protein_goal=goal.protein_goal,
        carbs_goal=goal.carbs_goal,
        fats_goal=goal.fats_goal
    )
    db.add(db_goal)
    db.commit()
    db.refresh(db_goal)
    return db_goal

def get_goals(db: Session):
    """Get all user goals."""
    return db.query(models.UserGoal).all()


# ---------- User Profiles ----------
def get_user_profile(db: Session, profile_id: int):
    """Get a user profile by ID."""
    return db.query(models.UserProfile).filter(models.UserProfile.id == profile_id).first()

def get_user_profiles(db: Session, skip: int = 0, limit: int = 100):
    """Get all user profiles."""
    return db.query(models.UserProfile).offset(skip).limit(limit).all()
