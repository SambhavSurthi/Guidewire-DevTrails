import uuid
from sqlalchemy import Column, String, Integer, Numeric, Boolean, Enum, DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum

class EventType(str, enum.Enum):
    heavy_rain = "heavy_rain"
    extreme_heat = "extreme_heat"
    flood = "flood"
    severe_aqi = "severe_aqi"
    curfew = "curfew"
    app_outage = "app_outage"

class SeverityLevel(str, enum.Enum):
    watch = "watch"
    warning = "warning"
    critical = "critical"

class DisruptionEvent(Base):
    __tablename__ = "disruption_events"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    event_type = Column(Enum(EventType, native_enum=False), nullable=False)
    zone = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    severity = Column(Enum(SeverityLevel, native_enum=False))
    
    value = Column(Numeric(10, 2))
    threshold = Column(Numeric(10, 2))
    data_source = Column(String(100))
    
    started_at = Column(DateTime, nullable=False)
    ended_at = Column(DateTime)
    is_active = Column(Boolean, default=True)
    
    workability_score = Column(Integer)
    created_at = Column(DateTime, server_default=func.now())
