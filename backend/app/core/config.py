from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "GigGuard X"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # DATABASE
    DATABASE_URL: str = "postgresql+asyncpg://gigguard:gigguard123@localhost:5432/gigguard_db"
    DATABASE_SYNC_URL: str = "postgresql://gigguard:gigguard123@localhost:5432/gigguard_db"
    
    # REDIS
    REDIS_URL: str = "redis://localhost:6379/0"
    
    # CELERY
    CELERY_BROKER_URL: str = "redis://localhost:6379/1"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/2"
    
    # JWT AUTH
    SECRET_KEY: str = "super_secret_temporary_key_for_gigguard_x"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7 # 7 days
    
    # CORS
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:5173", "http://localhost:3000"]

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True, extra="ignore")

settings = Settings()
