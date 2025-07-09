def input_node(state):
    return {"input_data": state["input_data"]}

def process_node(state):
    input_data = state["input_data"]

    today = input_data["today"]
    yesterday = input_data["yesterday"]

    profit = today["revenue"] - today["cost"]

    revenue_change = ((today["revenue"] - yesterday["revenue"]) / yesterday["revenue"]) * 100
    cost_change = ((today["cost"] - yesterday["cost"]) / yesterday["cost"]) * 100

    today_cac = today["cost"] / today["customers"]
    yesterday_cac = yesterday["cost"] / yesterday["customers"]
    cac_change = ((today_cac - yesterday_cac) / yesterday_cac) * 100

    processed_data = {
        "profit": profit,
        "revenue_change_percent": revenue_change,
        "cost_change_percent": cost_change,
        "today_cac": today_cac,
        "yesterday_cac": yesterday_cac,
        "cac_change_percent": cac_change
    }

    return {"processed_data": processed_data}

def recommendation_node(state):
    data = state["processed_data"]
    recommendations = []
    alerts = []

    if data["profit"] < 0:
        alerts.append("Negative profit detected.")
        recommendations.append("Consider reducing operational costs.")

    if data["cac_change_percent"] > 20:
        alerts.append("CAC has increased more than 20%.")
        recommendations.append("Review your marketing strategies.")

    if data["revenue_change_percent"] > 10:
        recommendations.append("Sales are growing, consider increasing the advertising budget.")

    return {
        "recommendation": {
            "summary": data,
            "alerts": alerts,
            "recommendations": recommendations
        }
    }
