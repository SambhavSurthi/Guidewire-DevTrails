import uuid
from sqlalchemy import Column, String, Integer, Numeric, Boolean, Enum, DateTime, Date, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum

class PolicyStatus(str, enum.Enum):
    active = "active"
    expired = "expired"
    cancelled = "cancelled"

class PlanTier(str, enum.Enum):
    basic = "basic"
    standard = "standard"
    full = "full"

class Policy(Base):
    __tablename__ = "policies"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    policy_number = Column(String(50), unique=True, nullable=False)
    worker_id = Column(UUID(as_uuid=True), ForeignKey("worker_profiles.id"), nullable=False)
    
    status = Column(Enum(PolicyStatus, native_enum=False), default=PolicyStatus.active)
    plan_tier = Column(Enum(PlanTier, native_enum=False), nullable=False)
    
    weekly_premium = Column(Numeric(8, 2), nullable=False)
    coverage_amount = Column(Numeric(10, 2), nullable=False)
    
    week_start = Column(Date, nullable=False)
    week_end = Column(Date, nullable=False)
    
    risk_score_at_creation = Column(Integer)
    auto_renew = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())
    
    worker = relationship("WorkerProfile", backref="policies")
