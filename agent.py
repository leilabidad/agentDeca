from langgraph.graph import StateGraph
from nodes import input_node, process_node, recommendation_node

# Define the initial state schema
state = {
    "input_data": None,
    "processed_data": None,
    "recommendation": None,
}

# Build the graph
builder = StateGraph(state)
builder.add_node("input", input_node)
builder.add_node("process", process_node)
builder.add_node("recommend", recommendation_node)

builder.set_entry_point("input")
builder.add_edge("input", "process")
builder.add_edge("process", "recommend")

builder.set_finish_point("recommend")

# Compile the graph
app = builder.compile()

if __name__ == "__main__":
    import json

    # Load sample data
    with open("data.json", "r") as f:
        sample_input = json.load(f)["input_data"]

    # Run the agent
    result = app.invoke({"input_data": sample_input})

    # Output the result
    print(json.dumps(result["recommendation"], indent=2))
