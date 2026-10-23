from fastapi import APIRouter, Response
from prometheus_client import CONTENT_TYPE_LATEST, Counter, Histogram, generate_latest

router = APIRouter()

WEBHOOK_REQUESTS = Counter(
    "hetupr_webhook_requests_total",
    "Total incoming GitHub webhook requests",
    ["event", "status"],
)

REVIEW_DURATION = Histogram(
    "hetupr_review_duration_seconds",
    "Duration of PR review analysis in seconds",
)


@router.get("/")
def get_metrics():
    """Prometheus metrics scrape endpoint."""
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)
