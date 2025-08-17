# app/routers/user_profiles.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas, utils
from app.database import get_db

router = APIRouter(prefix="/profiles", tags=["User Profiles"])

@router.post("/", response_model=schemas.UserProfileResponse)
def create_profile(profile: schemas.UserProfileCreate, db: Session = Depends(get_db)):
    # Calculate targets
    cals, protein, carbs, fats = utils.calculate_targets(
        profile.age, profile.gender, profile.height_cm,
        profile.weight_kg, profile.activity_level, profile.goal
    )

    new_profile = models.UserProfile(
        name=profile.name,
        age=profile.age,
        gender=profile.gender,
        height_cm=profile.height_cm,
        weight_kg=profile.weight_kg,
        activity_level=profile.activity_level,
        goal=profile.goal,
        target_calories=cals,
        target_protein=protein,
        target_carbs=carbs,
        target_fats=fats
    )
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    return new_profile
