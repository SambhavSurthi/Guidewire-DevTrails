import uuid
from sqlalchemy import Column, String, Numeric, Enum, DateTime, Text, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum

class WalletTransactionType(str, enum.Enum):
    deposit = "deposit"
    withdrawal = "withdrawal"
    cashback = "cashback"

class IncomeBufferWallet(Base):
    __tablename__ = "income_buffer_wallet"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    worker_id = Column(UUID(as_uuid=True), ForeignKey("worker_profiles.id"), unique=True, nullable=False)
    
    balance = Column(Numeric(10, 2), default=0)
    total_deposited = Column(Numeric(10, 2), default=0)
    total_withdrawn = Column(Numeric(10, 2), default=0)
    
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    worker = relationship("WorkerProfile", backref="wallet", uselist=False)

class WalletTransaction(Base):
    __tablename__ = "wallet_transactions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    wallet_id = Column(UUID(as_uuid=True), ForeignKey("income_buffer_wallet.id"), nullable=False)
    
    type = Column(Enum(WalletTransactionType, native_enum=False), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    description = Column(Text)
    
    related_claim_id = Column(UUID(as_uuid=True), ForeignKey("claims.id"), nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    
    wallet = relationship("IncomeBufferWallet", backref="transactions")
    claim = relationship("Claim")
