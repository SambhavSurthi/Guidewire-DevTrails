from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class WorkerOnboardRequest(BaseModel):
    platform: str
    delivery_category: str
    partner_id: str
    city: str
    zone: str
    latitude: float
    longitude: float
    vehicle_type: str
    daily_hours: int
    avg_weekly_earnings: float
    months_active: int
    aadhaar_last4: str

class WorkerOnboardResponse(BaseModel):
    worker_profile: dict
    risk_score: int
    risk_category: str
    recommended_plan: str
    weekly_premium: int
    coverage_amount: int

@router.post("/onboard", response_model=WorkerOnboardResponse, status_code=status.HTTP_201_CREATED)
async def onboard_worker(data: WorkerOnboardRequest):
    # Mocking implementation for Phase 1
    worker_profile = data.model_dump()
    worker_profile["id"] = "mocked-uuid"
    
    return {
        "worker_profile": worker_profile,
        "risk_score": 62,
        "risk_category": "medium_high",
        "recommended_plan": "standard",
        "weekly_premium": 89,
        "coverage_amount": 1250
    }

@router.get("/me/insights")
async def get_insights():
    return {
        "workability_score": 70,
        "score_breakdown": {
            "weather": 65, "aqi": 72, "traffic": 80, "demand": 68
        },
        "income_forecast": {
            "today": { "low": 480, "high": 560, "disruption_risk": 0.68 },
            "week": { "low": 3200, "high": 3500 }
        },
        "alerts": [
            { "type": "rain", "message": "Heavy rain forecast tomorrow 2pm-6pm", "probability": 0.68 }
        ],
        "recommendations": [
            { "icon": "clock", "title": "Best working window", "text": "11am-2pm, 6pm-9pm" },
            { "icon": "map", "title": "Safer zone nearby", "text": "Secunderabad - 40% lower flood risk" }
        ],
        "best_working_hours": ["11:00", "14:00", "18:00", "21:00"]
    }
