from langgraph.graph import StateGraph

from agents.classifier_agent import classifier
from agents.summarizer_agent import summarizer
# Add imports for other agents if you have more

from schemas import AgentState, ToolDecision

# Define a tool_router based on classifier output
def tool_router(state: AgentState) -> str:
    decision = state.tool_decision
    if decision.tool_name == "summarizer":
        return "summarizer"
    # Extend with more routes for other tools
    return "end"

# Build workflow graph
builder = StateGraph(AgentState)
builder.add_node("classifier", classifier)
builder.add_node("summarizer", summarizer)

builder.set_entry_point("classifier")
builder.add_conditional_edges("classifier", tool_router)
builder.add_edge("summarizer", "end")

builder.add_node("end", lambda x: x)
workflow = builder.compile()