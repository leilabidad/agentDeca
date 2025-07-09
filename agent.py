from langgraph.graph import StateGraph
from typing import TypedDict, List
from langchain_core.runnables import RunnableLambda

# Define the state schema
class AgentState(TypedDict):
    daily_revenue: float
    daily_cost: float
    previous_revenue: float
    previous_cost: float
    number_of_customers: int
    profit: float
    alerts: List[str]
    recommendations: List[str]

# Function: Calculate profit
def calculate_profit(state: AgentState) -> AgentState:
    profit = state["daily_revenue"] - state["daily_cost"]
    state["profit"] = profit
    return state

# Function: Generate alerts
def generate_alerts(state: AgentState) -> AgentState:
    alerts = []
    if state["daily_cost"] > state["daily_revenue"]:
        alerts.append("Costs exceed revenue!")
    if state["number_of_customers"] < 10:
        alerts.append("Low number of customers.")
    state["alerts"] = alerts
    return state

# Function: Generate recommendations
def generate_recommendations(state: AgentState) -> AgentState:
    recommendations = []
    if state["daily_revenue"] < state["previous_revenue"]:
        recommendations.append("Consider improving marketing strategies.")
    if state["daily_cost"] > state["previous_cost"]:
        recommendations.append("Analyze cost increase.")
    if state["profit"] < 500:
        recommendations.append("Improve sales or reduce costs.")
    state["recommendations"] = recommendations
    return state

# Build the LangGraph graph
builder = StateGraph(AgentState)

# Add steps
builder.add_node("calculate_profit", RunnableLambda(calculate_profit))
builder.add_node("generate_alerts", RunnableLambda(generate_alerts))
builder.add_node("generate_recommendations", RunnableLambda(generate_recommendations))

# Define flow
builder.set_entry_point("calculate_profit")
builder.add_edge("calculate_profit", "generate_alerts")
builder.add_edge("generate_alerts", "generate_recommendations")
builder.set_finish_point("generate_recommendations")

# Compile the graph
app = builder.compile()
