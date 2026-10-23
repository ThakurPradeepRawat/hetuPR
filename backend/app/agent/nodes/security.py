from app.agent.schemas import CandidateFinding, ReviewState


async def analyze_security(state: ReviewState) -> dict:
    """Security analysis node: scans diff for SQLi, SSRF, secret leaks, auth flaws."""
    # Placeholder for LLM/AST-driven security analysis
    findings: list[CandidateFinding] = []
    return {"candidate_findings": state.candidate_findings + findings}
