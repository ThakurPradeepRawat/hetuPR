import hashlib
import hmac
import pytest
from httpx import AsyncClient

from app.core.config import settings
from app.core.security import verify_webhook_signature


def test_signature_verification():
    secret = "test_webhook_secret"
    payload = b'{"action": "opened"}'
    valid_sig = "sha256=" + hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()

    assert verify_webhook_signature(payload, valid_sig, secret) is True
    assert verify_webhook_signature(payload, "sha256=invalid", secret) is False
    assert verify_webhook_signature(payload, None, secret) is False


@pytest.mark.asyncio
async def test_health_endpoint(client: AsyncClient):
    response = await client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


@pytest.mark.asyncio
async def test_webhook_invalid_signature(client: AsyncClient):
    response = await client.post(
        "/api/v1/webhooks/github",
        headers={
            "X-GitHub-Event": "pull_request",
            "X-Hub-Signature-256": "sha256=wrongsignature",
            "X-GitHub-Delivery": "del-12345",
        },
        json={"action": "opened"},
    )
    assert response.status_code == 401
