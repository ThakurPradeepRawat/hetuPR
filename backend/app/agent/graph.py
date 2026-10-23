from langgraph.graph import END, StateGraph

from app.agent.nodes.critic import validate_findings
from app.agent.nodes.performance import analyze_performance
from app.agent.nodes.security import analyze_security
from app.agent.schemas import ReviewState


def build_review_graph():
    """Build the state graph for HetuPR code analysis and critique."""
    workflow = StateGraph(ReviewState)

    workflow.add_node("security_analysis", analyze_security)
    workflow.add_node("performance_analysis", analyze_performance)
    workflow.add_node("critic", validate_findings)

    workflow.set_entry_point("security_analysis")
    workflow.add_edge("security_analysis", "performance_analysis")
    workflow.add_edge("performance_analysis", "critic")
    workflow.add_edge("critic", END)

    return workflow.compile()
