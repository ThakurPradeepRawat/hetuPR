"""API v1 routers."""

from fastapi import APIRouter

from app.api.v1.metrics import router as metrics_router
from app.api.v1.repos import router as repos_router
from app.api.v1.webhooks import router as webhooks_router

api_router = APIRouter(prefix="/v1")
api_router.include_router(webhooks_router, prefix="/webhooks", tags=["Webhooks"])
api_router.include_router(repos_router, prefix="/repos", tags=["Repositories"])
api_router.include_router(metrics_router, prefix="/metrics", tags=["Metrics"])
