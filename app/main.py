from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, SessionLocal

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------- Food ----------
@app.post("/foods/", response_model=schemas.Food)
def create_food(food: schemas.FoodCreate, db: Session = Depends(get_db)):
    return crud.create_food(db=db, food=food)

@app.get("/foods/", response_model=list[schemas.Food])
def read_foods(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_foods(db, skip=skip, limit=limit)


# ---------- Daily Logs ----------
@app.post("/logs/", response_model=schemas.DailyLog)
def create_log(log: schemas.DailyLogCreate, db: Session = Depends(get_db)):
    return crud.create_daily_log(db=db, log=log)

@app.get("/logs/{date}", response_model=list[schemas.DailyLog])
def read_logs(date: str, db: Session = Depends(get_db)):
    return crud.get_logs_by_date(db=db, date=date)


# ---------- Goals ----------
@app.post("/goals/", response_model=schemas.UserGoal)
def set_goal(goal: schemas.UserGoalCreate, db: Session = Depends(get_db)):
    return crud.set_goal(db=db, goal=goal)

@app.get("/goals/", response_model=list[schemas.UserGoal])
def get_goals(db: Session = Depends(get_db)):
    return crud.get_goals(db=db)
