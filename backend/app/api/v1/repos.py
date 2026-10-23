from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import ReviewAudit
from app.db.session import get_db

router = APIRouter()


@router.get("/")
async def list_repositories():
    """List tracked repositories."""
    return {"repositories": []}


@router.get("/{repo_name:path}/audits")
async def list_repo_audits(repo_name: str, db: AsyncSession = Depends(get_db)):
    """List review audits for a repository."""
    stmt = select(ReviewAudit).where(ReviewAudit.repo_name == repo_name).limit(50)
    result = await db.execute(stmt)
    audits = result.scalars().all()
    return {"repo": repo_name, "audits": audits}
