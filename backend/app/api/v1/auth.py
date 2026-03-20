from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.database import get_db
from app.core.security import verify_password, get_password_hash, create_custom_token
from app.models.user import User, UserRole
from app.models.worker import WorkerProfile
from app.schemas.user import UserCreate, UserLogin, RegisterResponse, LoginResponse, UserResponse
import uuid

router = APIRouter()

@router.post("/register", response_model=RegisterResponse, status_code=status.HTTP_201_CREATED)
async def register(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where((User.email == user_in.email) | (User.phone == user_in.phone)))
    existing_user = result.scalars().first()
    
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email or phone already exists in the system",
        )
    
    hashed_password = get_password_hash(user_in.password)
    user = User(
        email=user_in.email,
        phone=user_in.phone,
        hashed_password=hashed_password,
        role=UserRole(user_in.role) if user_in.role in ["worker", "admin", "insurer"] else UserRole.worker
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    
    # Generate tokens
    payload = {
        "sub": str(user.id),
        "role": user.role.value,
        "jti": str(uuid.uuid4())
    }
    access_token = create_custom_token(payload)
    refresh_token = create_custom_token({**payload, "is_refresh": True})
    
    return {
        "user_id": str(user.id),
        "email": user.email,
        "role": user.role.value,
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

@router.post("/login", response_model=LoginResponse)
async def login(user_in: UserLogin, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == user_in.email))
    user = result.scalars().first()
    
    if not user or not verify_password(user_in.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")

    # Fetch worker profile if exists
    profile_result = await db.execute(select(WorkerProfile).where(WorkerProfile.user_id == user.id))
    worker_profile = profile_result.scalars().first()
    
    profile_data = None
    if worker_profile:
        profile_data = {
            "id": str(worker_profile.id),
            "full_name": worker_profile.full_name,
            "city": worker_profile.city,
            "zone": worker_profile.zone,
            "risk_score": worker_profile.risk_score,
            "trust_score": worker_profile.trust_score
        }

    # Generate tokens
    payload = {
        "sub": str(user.id),
        "role": user.role.value,
        "worker_id": str(worker_profile.id) if worker_profile else None,
        "jti": str(uuid.uuid4())
    }
    
    access_token = create_custom_token(payload)
    refresh_token = create_custom_token({**payload, "is_refresh": True})
    
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "user": user,
        "worker_profile": profile_data
    }

@router.post("/refresh")
async def refresh():
    return {"message": "Not implemented yet"}
