"""Utility functions for the application."""

from dataclasses import dataclass
from . import models

@dataclass
class UserProfileData:
    """Data class for user profile."""
    age: int
    gender: str
    height_cm: float
    weight_kg: float
    activity_level: str
    goal: str

def calculate_targets(profile: UserProfileData):
    """Calculate the target calories, protein, carbs, and fats for a user."""
    # Mifflin-St Jeor BMR
    if profile.gender.lower() == "male":
        bmr = 10 * profile.weight_kg + 6.25 * profile.height_cm - 5 * profile.age + 5
    else:
        bmr = 10 * profile.weight_kg + 6.25 * profile.height_cm - 5 * profile.age - 161

    activity_multipliers = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725,
        "very_active": 1.9,
    }
    tdee = bmr * activity_multipliers.get(profile.activity_level, 1.2)

    if profile.goal == "loss":
        calories = tdee - 500
    elif profile.goal == "gain":
        calories = tdee + 500
    else:
        calories = tdee

    protein = (calories * 0.20) / 4
    carbs = (calories * 0.50) / 4
    fats = (calories * 0.30) / 9

    return calories, protein, carbs, fats


def calculate_goals(db, log_date):
    """Aggregate totals for a given date from DailyLog * Food."""
    logs = db.query(models.DailyLog).filter(models.DailyLog.date == log_date).all()
    totals = {"calories": 0.0, "protein": 0.0, "carbs": 0.0, "fats": 0.0}

    for log in logs:
        food = log.food
        totals["calories"] += log.quantity * food.calories
        totals["protein"]  += log.quantity * food.protein
        totals["carbs"]    += log.quantity * food.carbs
        totals["fats"]     += log.quantity * food.fats

    return totals
