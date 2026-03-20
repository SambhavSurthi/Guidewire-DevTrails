import uuid
from sqlalchemy import Column, String, Integer, Numeric, Enum, DateTime, Text, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum

class ClaimStatus(str, enum.Enum):
    initiated = "initiated"
    fraud_check = "fraud_check"
    pow_check = "pow_check"
    approved = "approved"
    rejected = "rejected"
    paid = "paid"
    flagged = "flagged"
    appealing = "appealing"

class Claim(Base):
    __tablename__ = "claims"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    claim_number = Column(String(50), unique=True, nullable=False)
    
    policy_id = Column(UUID(as_uuid=True), ForeignKey("policies.id"), nullable=False)
    worker_id = Column(UUID(as_uuid=True), ForeignKey("worker_profiles.id"), nullable=False)
    disruption_id = Column(UUID(as_uuid=True), ForeignKey("disruption_events.id"))
    
    status = Column(Enum(ClaimStatus, native_enum=False), default=ClaimStatus.initiated)
    trigger_type = Column(String(50))
    trigger_value = Column(Numeric(10, 2))
    duration_hours = Column(Numeric(5, 2))
    
    estimated_loss = Column(Numeric(10, 2))
    payout_amount = Column(Numeric(10, 2))
    payout_percentage = Column(Integer)
    
    fraud_score = Column(Integer, default=0)
    pow_score = Column(Integer, default=0)
    history_score = Column(Integer, default=0)
    trust_score = Column(Integer, default=0)
    
    fraud_flags = Column(JSONB, default=list)
    pow_signals = Column(JSONB, default=dict)
    rejection_reason = Column(Text)
    
    initiated_at = Column(DateTime, server_default=func.now())
    approved_at = Column(DateTime)
    paid_at = Column(DateTime)
    created_at = Column(DateTime, server_default=func.now())
    
    policy = relationship("Policy", backref="claims")
    worker = relationship("WorkerProfile", backref="claim_records")
    disruption = relationship("DisruptionEvent", backref="claims")
