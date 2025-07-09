import unittest
from agent import app

class TestBusinessAgent(unittest.TestCase):

    def setUp(self):
        self.test_data = {
            "today": {
                "revenue": 1500,
                "cost": 1000,
                "customers": 50
            },
            "yesterday": {
                "revenue": 1200,
                "cost": 800,
                "customers": 40
            }
        }

    def test_output_structure(self):
        result = app.invoke({"input_data": self.test_data})
        output = result["recommendation"]

        self.assertIn("summary", output)
        self.assertIn("alerts", output)
        self.assertIn("recommendations", output)

    def test_profit_calculation(self):
        result = app.invoke({"input_data": self.test_data})
        summary = result["recommendation"]["summary"]
        expected_profit = 500
        self.assertEqual(summary["profit"], expected_profit)

    def test_alerts_and_recommendations(self):
        result = app.invoke({"input_data": self.test_data})
        output = result["recommendation"]

        self.assertIsInstance(output["alerts"], list)
        self.assertIsInstance(output["recommendations"], list)

if __name__ == "__main__":
    unittest.main()
