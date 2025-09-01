from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import crud, schemas
from .database import get_db, engine, Base
from .user_profiles import router as profiles_router
from .recommendations import router as recommendations_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Nutrition API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(profiles_router)
app.include_router(recommendations_router)

# Foods
@app.post("/foods/", response_model=schemas.Food)
def create_food(food: schemas.FoodCreate, db: Session = Depends(get_db)):
    return crud.create_food(db=db, food=food)

@app.get("/foods/", response_model=list[schemas.Food])
def read_foods(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_foods(db=db, skip=skip, limit=limit)

# Daily Logs
@app.post("/logs/", response_model=schemas.DailyLog)
def create_log(log: schemas.DailyLogCreate, db: Session = Depends(get_db)):
    return crud.create_daily_log(db=db, log=log)

@app.get("/logs/", response_model=list[schemas.DailyLog])
def read_logs(date: str, db: Session = Depends(get_db)):
    return crud.get_logs_by_date(db=db, date=date)

# Goals
@app.post("/goals/", response_model=schemas.UserGoal)
def set_goal(goal: schemas.UserGoalCreate, db: Session = Depends(get_db)):
    return crud.set_goal(db=db, goal=goal)

@app.get("/goals/all/", response_model=list[schemas.UserGoal])
def get_all_goals(db: Session = Depends(get_db)):
    return db.query(crud.models.UserGoal).all()

@app.get("/goals/{user_id}", response_model=list[schemas.UserGoal])
def get_user_goals(user_id: int, db: Session = Depends(get_db)):
    return crud.get_goals(db=db, user_id=user_id)
