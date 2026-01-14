from typing import TypedDict, Optional
from langgraph.graph import StateGraph, END
from agent.intents import detect_intent
from agent.rag import get_rag_answer
from agent.tools import mock_lead_capture
class AgentState(TypedDict):
    messages: list
    intent: Optional[str]
    name: Optional[str]
    email: Optional[str]
    platform: Optional[str]
def detect_intent_node(state, llm):
    last_user_msg = state["messages"][-1]["content"]
    intent = detect_intent(llm, last_user_msg)
    state["intent"] = intent
    return state
def greeting_node(state, llm):
    state["messages"].append({
        "role": "assistant",
        "content": "Hello! I’m the AutoStream assistant. How can I help you today?"
    })
    return state
def rag_node(state, llm, vectorstore):
    user_msg = state["messages"][-1]["content"]
    answer = get_rag_answer(vectorstore, user_msg, llm)
    state["messages"].append({
        "role": "assistant",
        "content": answer
    })
    return state
def ask_name_node(state, llm):
    state["messages"].append({
        "role": "assistant",
        "content": "That’s awesome! May I know your name?"
    })
    return state
def ask_email_node(state, llm):
    state["messages"].append({
        "role": "assistant",
        "content": "Thanks! Could you share your email address?"
    })
    return state
def ask_platform_node(state, llm):
    state["messages"].append({
        "role": "assistant",
        "content": "Great. Which creator platform do you primarily use? (YouTube, Instagram, etc.)"
    })
    return state
def capture_lead_node(state, llm):
    mock_lead_capture(state["name"], state["email"], state["platform"])
    state["messages"].append({
        "role": "assistant",
        "content": "You're all set! Our team will reach out to you shortly."
    })
    return state
def route(state: AgentState):
    if state["intent"] == "high_intent":
        if not state.get("name"):
            return "ask_name"
        if not state.get("email"):
            return "ask_email"
        if not state.get("platform"):
            return "ask_platform"
        return "capture_lead"
    if state["intent"] == "greeting":
        return "greeting"
    return "rag"
def build_graph(llm, vectorstore):
    graph = StateGraph(AgentState)
    graph.add_node("detect_intent", lambda s: detect_intent_node(s, llm))
    graph.add_node("greeting", lambda s: greeting_node(s, llm))
    graph.add_node("rag", lambda s: rag_node(s, llm, vectorstore))
    graph.add_node("ask_name", lambda s: ask_name_node(s, llm))
    graph.add_node("ask_email", lambda s: ask_email_node(s, llm))
    graph.add_node("ask_platform", lambda s: ask_platform_node(s, llm))
    graph.add_node("capture_lead", lambda s: capture_lead_node(s, llm))
    graph.set_entry_point("detect_intent")
    graph.add_conditional_edges(
        "detect_intent",
        route,
        {
            "greeting": "greeting",
            "rag": "rag",
            "ask_name": "ask_name",
            "ask_email": "ask_email",
            "ask_platform": "ask_platform",
            "capture_lead": "capture_lead",
        },
    )
    graph.add_edge("greeting", END)
    graph.add_edge("rag", END)
    graph.add_edge("ask_name", END)
    graph.add_edge("ask_email", END)
    graph.add_edge("ask_platform", END)
    graph.add_edge("capture_lead", END)
    return graph.compile()