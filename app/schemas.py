from pydantic import BaseModel
from datetime import date

# ---------- Food ----------
class FoodBase(BaseModel):
    name: str
    barcode: str | None = None
    calories: float
    protein: float
    carbs: float
    fats: float

class FoodCreate(FoodBase):
    pass

class Food(FoodBase):
    id: int

    class Config:
        from_attributes = True   # ✅ pydantic v2 fix


# ---------- Daily Log ----------
class DailyLogBase(BaseModel):
    food_id: int
    quantity: float
    date: date

class DailyLogCreate(DailyLogBase):
    pass

class DailyLog(DailyLogBase):
    id: int
    food: Food

    class Config:
        from_attributes = True


# ---------- Totals ----------
class DailyTotals(BaseModel):
    date: date
    calories: float
    protein: float
    carbs: float
    fats: float


# ---------- User Goal ----------
class UserGoalBase(BaseModel):
    calories_goal: float
    protein_goal: float
    carbs_goal: float
    fats_goal: float

class UserGoalCreate(UserGoalBase):
    pass

class UserGoal(UserGoalBase):
    id: int

    class Config:
        from_attributes = True
