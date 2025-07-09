# Simple AI Business Agent using LangGraph

This project implements a simple AI agent that analyzes basic business data (daily sales and costs) and generates summary reports with actionable recommendations. It is built using the LangGraph framework.

## Features

- Calculates daily profit
- Computes percentage changes in revenue and cost compared to the previous day
- Calculates Customer Acquisition Cost (CAC) changes
- Provides alerts and business recommendations based on the data

## Setup Instructions

1. **Clone the repository**

```bash
git clone <repository-url>
cd <repository-folder>
Create a virtual environment and activate it
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
Install dependencies
pip install -r requirements.txt
Run the agent
python agent.py
You should see a JSON output with profit summary, alerts, and recommendations.

Running Tests
python -m unittest test_agent.py
Project Structure
ai-agent-langgraph/
├── agent.py           # Main agent program building the LangGraph graph
├── nodes.py           # Nodes defining the graph logic
├── test_agent.py      # Unit tests for the agent
├── data.json          # Sample input data for testing
├── requirements.txt   # Python dependencies
└── README.md          # This file
Notes
This project uses LangGraph, a framework to build AI agents using state graphs.
The project is completely free and uses no paid APIs.
Feel free to ask if you want me to help with any additional setup or deployment!

