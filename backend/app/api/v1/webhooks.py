import json
from fastapi import APIRouter, Header, HTTPException, Request, status

from app.core.config import settings
from app.core.logging import logger
from app.core.ratelimit import check_idempotency, get_redis
from app.core.security import verify_webhook_signature

router = APIRouter()


@router.post("/github", status_code=status.HTTP_202_ACCEPTED)
async def handle_github_webhook(
    request: Request,
    x_github_event: str = Header(..., alias="X-GitHub-Event"),
    x_hub_signature_256: str = Header(None, alias="X-Hub-Signature-256"),
    x_github_delivery: str = Header(..., alias="X-GitHub-Delivery"),
):
    """Handle incoming GitHub PR webhook with signature verification and idempotency."""
    body_bytes = await request.body()

    if not verify_webhook_signature(body_bytes, x_hub_signature_256, settings.GITHUB_WEBHOOK_SECRET):
        logger.warning("Rejected webhook due to invalid signature", delivery=x_github_delivery)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid signature")

    # Check idempotency
    if not await check_idempotency(x_github_delivery):
        logger.info("Ignoring duplicate webhook delivery", delivery=x_github_delivery)
        return {"status": "duplicate_ignored"}

    payload = await request.json()

    # Only process pull_request events
    if x_github_event == "pull_request":
        action = payload.get("action")
        if action in ("opened", "synchronize", "reopened"):
            client = await get_redis()
            job_payload = {
                "delivery_id": x_github_delivery,
                "action": action,
                "pr_number": payload.get("number"),
                "repo": payload.get("repository", {}).get("full_name"),
                "head_sha": payload.get("pull_request", {}).get("head", {}).get("sha"),
            }
            await client.rpush("hetupr:review_jobs", json.dumps(job_payload))
            logger.info("Enqueued PR review job", delivery=x_github_delivery, action=action)

    return {"status": "accepted", "delivery_id": x_github_delivery}
