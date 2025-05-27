from langgraph.graph import StateGraph
from schema import UserQuery
from agents.classifier_agent import classifier
from agents.summarizer_agent import summarizer
from agents.search_agent import search_web
from agents.math_agent import calculate_expression
from agents.wiki_agent import lookup_wikipedia


def classify(state):
    return classifier.invoke({"question": state["question"]})

def use_tool(state):
    tool = state["tool"]
    question = state["question"]
    if tool == "search":
        return {"result": search_web(question)}
    elif tool == "math":
        return {"result": calculate_expression(question)}
    elif tool == "wiki":
        return {"result": lookup_wikipedia(question)}
    else:
        return {"result": "Unknown tool"}

def summarize(state):
    return summarizer.invoke({"result": state["result"]})


graph = StateGraph()

# Nodes
graph.add_node("classify", classify)
graph.add_node("tool_use", use_tool)
graph.add_node("summarize", summarize)

# Edges
graph.set_entry_point("classify")
graph.add_edge("classify", "tool_use")
graph.add_edge("tool_use", "summarize")

workflow = graph.compile()