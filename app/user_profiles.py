from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, utils, crud
from .database import get_db

router = APIRouter(prefix="/profiles", tags=["User Profiles"])

@router.post("/", response_model=schemas.UserProfileResponse)
def create_profile(profile: schemas.UserProfileCreate, db: Session = Depends(get_db)):
    profile_data = utils.UserProfileData(
        age=profile.age,
        gender=profile.gender,
        height_cm=profile.height_cm,
        weight_kg=profile.weight_kg,
        activity_level=profile.activity_level,
        goal=profile.goal,
    )
    cals, protein, carbs, fats = utils.calculate_targets(profile_data)

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

@router.get("/{profile_id}", response_model=schemas.UserProfileResponse)
def get_profile(profile_id: int, db: Session = Depends(get_db)):
    profile = crud.get_user_profile(db, profile_id)
    if not profile:
        raise HTTPException(status_code=404, detail="User profile not found")
    return profile

@router.get("/", response_model=list[schemas.UserProfileResponse])
def get_profiles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_user_profiles(db, skip=skip, limit=limit)
