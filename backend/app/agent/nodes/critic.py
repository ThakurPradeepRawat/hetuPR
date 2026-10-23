from app.agent.schemas import CandidateFinding, ReviewState


async def validate_findings(state: ReviewState) -> dict:
    """Critic stage: ensures findings correspond to changed lines, removes duplicates and false positives."""
    validated: list[CandidateFinding] = []

    seen = set()
    for finding in state.candidate_findings:
        # Deduplication key
        key = (finding.file_path, finding.line_number, finding.title)
        if key in seen:
            continue

        # Verify line is in changed_lines (if mapping exists)
        if state.changed_lines and finding.file_path in state.changed_lines:
            if finding.line_number not in state.changed_lines[finding.file_path]:
                continue

        # Confidence filter
        if finding.confidence < 0.7:
            continue

        seen.add(key)
        validated.append(finding)

    return {"validated_findings": validated}
