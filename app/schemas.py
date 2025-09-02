from datetime import date
from typing import Optional, List
from pydantic import BaseModel

# ---------- Food ----------
class FoodBase(BaseModel):
    name: str
    calories: float
    protein: float
    carbs: float
    fats: float

class FoodCreate(FoodBase):
    barcode: Optional[str] = None

class Food(FoodBase):
    id: int
    class Config:
        from_attributes = True

# ---------- Daily Logs ----------
class DailyLogBase(BaseModel):
    date: date
    quantity: float
    food_id: int
    user_id: int

class DailyLogCreate(DailyLogBase):
    pass

class DailyLog(DailyLogBase):
    id: int
    food: Optional[Food] = None
    class Config:
        from_attributes = True

# ---------- User Goals ----------
class UserGoalBase(BaseModel):
    user_id: Optional[int] = None
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

# ---------- User Profiles ----------
class UserProfileBase(BaseModel):
    name: str
    age: int
    weight_kg: float
    height_cm: float
    gender: str
    activity_level: str
    goal: Optional[str] = None

class UserProfileCreate(UserProfileBase):
    pass

class UserProfile(UserProfileBase):
    id: int
    class Config:
        from_attributes = True
