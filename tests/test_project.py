import unittest

from reports import calculate_total_expenses
from budget_manager import get_remaining_budget


class TestExpenseManager(unittest.TestCase):

    def test_total_expenses(self):
        expenses = [
            {"name": "Lunch", "amount": 120, "category": "Food"},
            {"name": "Bus", "amount": 120, "category": "Transport"}
        ]

        result = calculate_total_expenses(expenses)

        self.assertEqual(result, 240)

    def test_remaining_budget(self):
        budget = 1000
        total_expense = 240

        result = get_remaining_budget(budget, total_expense)

        self.assertEqual(result, 760)

    def test_empty_expenses(self):
        expenses = []

        result = calculate_total_expenses(expenses)

        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()