from sqlalchemy.orm import Session
from . import models, schemas

# ---------- Food ----------
def create_food(db: Session, food: schemas.FoodCreate):
    db_food = models.Food(**food.dict())
    db.add(db_food)
    db.commit()
    db.refresh(db_food)
    return db_food

def get_foods(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Food).offset(skip).limit(limit).all()


# ---------- Daily Log ----------
def create_daily_log(db: Session, log: schemas.DailyLogCreate):
    db_log = models.DailyLog(**log.dict())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

def get_logs_by_date(db: Session, date: str):
    return db.query(models.DailyLog).filter(models.DailyLog.date == date).all()


# ---------- User Goal ----------
def set_goal(db: Session, goal: schemas.UserGoalCreate):
    db_goal = models.UserGoal(**goal.dict())
    db.add(db_goal)
    db.commit()
    db.refresh(db_goal)
    return db_goal

def get_goals(db: Session):
    return db.query(models.UserGoal).all()
