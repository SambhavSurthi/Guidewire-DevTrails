import uuid
from sqlalchemy import Column, String, Numeric, Enum, DateTime, Text, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum

class PayoutStatus(str, enum.Enum):
    pending = "pending"
    processing = "processing"
    success = "success"
    failed = "failed"

class Payout(Base):
    __tablename__ = "payouts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    claim_id = Column(UUID(as_uuid=True), ForeignKey("claims.id"), nullable=False)
    worker_id = Column(UUID(as_uuid=True), ForeignKey("worker_profiles.id"), nullable=False)
    
    amount = Column(Numeric(10, 2), nullable=False)
    upi_id = Column(String(100))
    
    razorpay_payout_id = Column(String(100))
    razorpay_fund_account_id = Column(String(100))
    
    status = Column(Enum(PayoutStatus, native_enum=False), default=PayoutStatus.pending)
    failure_reason = Column(Text)
    
    processed_at = Column(DateTime)
    created_at = Column(DateTime, server_default=func.now())
    
    claim = relationship("Claim", backref="payout_record", uselist=False)
    worker = relationship("WorkerProfile")
