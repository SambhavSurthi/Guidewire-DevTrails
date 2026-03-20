from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from typing import Optional, List

router = APIRouter()

class PolicyCreateRequest(BaseModel):
    plan_tier: str = "standard"
    auto_renew: bool = True

class PolicyResponse(BaseModel):
    policy_number: str
    weekly_premium: int
    coverage_amount: int
    week_start: str
    week_end: str
    premium_breakdown: dict
    triggers_active: List[str]
    wallet_contribution: float

@router.post("/create", response_model=PolicyResponse, status_code=status.HTTP_201_CREATED)
async def create_policy(data: PolicyCreateRequest):
    # Mocking implementation for Phase 1
    return {
        "policy_number": "GS-2026-HYD-04821",
        "weekly_premium": 89,
        "coverage_amount": 1250,
        "week_start": "2026-03-17",
        "week_end": "2026-03-23",
        "premium_breakdown": {
            "base": 60, "zone_loading": 18, "hours_factor": 8,
            "seasonal": 3, "ai_discount": 0, "total": 89
        },
        "triggers_active": ["heavy_rain", "extreme_heat", "flood", "severe_aqi", "curfew", "app_outage"],
        "wallet_contribution": 8.90
    }
