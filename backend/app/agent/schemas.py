from typing import Annotated, Literal
from pydantic import BaseModel, Field


class CandidateFinding(BaseModel):
    file_path: str
    line_number: int
    category: Literal["security", "performance", "logic", "style"]
    severity: Literal["critical", "high", "medium", "low", "info"]
    title: str
    reasoning: str  # Indian logic 'Hetu' / Ground of conclusion
    confidence: float = Field(ge=0.0, le=1.0, default=1.0)


class ReviewState(BaseModel):
    repo_name: str
    pr_number: int
    head_sha: str
    diff_content: str
    changed_files: list[str] = Field(default_factory=list)
    changed_lines: dict[str, list[int]] = Field(default_factory=dict)
    candidate_findings: list[CandidateFinding] = Field(default_factory=list)
    validated_findings: list[CandidateFinding] = Field(default_factory=list)
    summary: str = ""
