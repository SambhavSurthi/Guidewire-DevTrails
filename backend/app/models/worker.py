import uuid
from sqlalchemy import Column, String, Integer, Numeric, Enum, DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum

class PlatformEnum(str, enum.Enum):
    swiggy = "swiggy"
    zomato = "zomato"
    zepto = "zepto"
    blinkit = "blinkit"
    amazon = "amazon"
    flipkart = "flipkart"

class DeliveryCategory(str, enum.Enum):
    food = "food"
    grocery = "grocery"
    ecommerce = "ecommerce"

class VehicleType(str, enum.Enum):
    bike = "bike"
    ev_scooter = "ev_scooter"
    bicycle = "bicycle"

class PreferredLanguage(str, enum.Enum):
    en = "en"
    hi = "hi"
    te = "te"

class WorkerProfile(Base):
    __tablename__ = "worker_profiles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), unique=True, nullable=False)
    full_name = Column(String(255), nullable=False)
    aadhaar_last4 = Column(String(4))
    
    platform = Column(Enum(PlatformEnum, native_enum=False))
    delivery_category = Column(Enum(DeliveryCategory, native_enum=False))
    partner_id = Column(String(100))
    
    city = Column(String(100))
    zone = Column(String(100))
    latitude = Column(Numeric(10, 8))
    longitude = Column(Numeric(11, 8))
    
    vehicle_type = Column(Enum(VehicleType, native_enum=False))
    daily_hours = Column(Integer)  # 4, 8, 12
    avg_weekly_earnings = Column(Numeric(10, 2))
    months_active = Column(Integer)
    
    risk_score = Column(Integer, default=50)
    trust_score = Column(Integer, default=70)
    loyalty_xp = Column(Integer, default=0)
    loyalty_level = Column(Integer, default=1)
    
    preferred_language = Column(Enum(PreferredLanguage, native_enum=False), default=PreferredLanguage.en)
    
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    user = relationship("User", backref="worker_profile")
