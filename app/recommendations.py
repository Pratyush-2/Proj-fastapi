from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/recommendations", tags=["Recommendations"])

class RecommendationResponse(BaseModel):
    food_name: str
    reason: str
    suggested_alternative: str

@router.post("/", response_model=List[RecommendationResponse])
def get_recommendations():
    return [
        {"food_name": "Burger", "reason": "High in calories", "suggested_alternative": "Grilled chicken"},
        {"food_name": "Soda", "reason": "High in sugar", "suggested_alternative": "Water"}
    ]
