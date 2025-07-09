import unittest
from agent import app  # app باید از نوع LangGraph graph باشد

class TestBusinessAgent(unittest.TestCase):

    def setUp(self):
        self.test_data = {
            "daily_revenue": 1500,
            "daily_cost": 1000,
            "previous_revenue": 1200,
            "previous_cost": 800,
            "number_of_customers": 50
        }

    def test_output_structure(self):
        result = app.invoke(self.test_data)
        self.assertIn("profit", result)
        self.assertIn("alerts", result)
        self.assertIn("recommendations", result)

    def test_profit_calculation(self):
        result = app.invoke(self.test_data)
        expected_profit = 1500 - 1000
        self.assertEqual(result["profit"], expected_profit)

    def test_alerts_and_recommendations(self):
        result = app.invoke(self.test_data)
        self.assertIsInstance(result["alerts"], list)
        self.assertIsInstance(result["recommendations"], list)

if __name__ == "__main__":
    unittest.main()
