from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_application() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        openapi_url=f"{settings.API_V1_STR}/openapi.json"
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    from fastapi.requests import Request
    from fastapi.responses import JSONResponse
    
    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        logger.error(f"Global exception: {exc}")
        return JSONResponse(
            status_code=500,
            content={"error": "Internal Server Error", "detail": str(exc)},
        )

    from app.api.v1.auth import router as auth_router
    from app.api.v1.workers import router as workers_router
    from app.api.v1.policies import router as policies_router

    app.include_router(auth_router, prefix=f"{settings.API_V1_STR}/auth", tags=["auth"])
    app.include_router(workers_router, prefix=f"{settings.API_V1_STR}/workers", tags=["workers"])
    app.include_router(policies_router, prefix=f"{settings.API_V1_STR}/policies", tags=["policies"])

    @app.get(f"{settings.API_V1_STR}/health")
    async def health_check():
        return {"status": "ok", "app": settings.PROJECT_NAME, "version": settings.VERSION}

    return app

import redis.asyncio as aioredis
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Connect to Redis
    app.state.redis = await aioredis.from_url(settings.REDIS_URL, decode_responses=True)
    yield
    # Shutdown: Close Redis
    await app.state.redis.close()

# Update app creation to use lifespan
def get_application_with_lifespan() -> FastAPI:
    app = get_application()
    app.router.lifespan_context = lifespan
    return app

app = get_application_with_lifespan()
