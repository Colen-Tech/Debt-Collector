"""Tests for main.py. Run with: python -m unittest"""

import unittest
from unittest.mock import patch

from main import add_debt, ask_amount, balance, record_payment, total_owed

class DebtTests(unittest.TestCase):

    def test_add_debt(self):
        debts = []
        add_debt(debts, "Ali", 100)
        self.assertEqual(len(debts), 1)
        self.assertEqual(balance(debts[0]), 100)

    def test_payment_reduces_balance(self):
        debts = []
        add_debt(debts, "Ali", 100)
        record_payment(debts, "Ali", 40)
        self.assertEqual(balance(debts[0]), 60)

    def test_payment_for_unknown_name(self):
        self.assertFalse(record_payment([], "Nobody", 10))

    def test_total_owed(self):
        debts = []
        add_debt(debts, "Ali", 100)
        add_debt(debts, "Sara", 50)
        record_payment(debts, "Ali", 30)
        self.assertEqual(total_owed(debts), 120)

class AskAmountTests(unittest.TestCase):

    def test_valid_number(self):
        with patch("builtins.input", return_value="100"):
            self.assertEqual(ask_amount("Amount: "), 100)

    def test_text_then_valid_number(self):
        with patch("builtins.input", side_effect=["abc", "50"]):
            self.assertEqual(ask_amount("Amount: "), 50)

    def test_zero_and_negative_then_valid_number(self):
        with patch("builtins.input", side_effect=["0", "-5", "25"]):
            self.assertEqual(ask_amount("Amount: "), 25)

    def test_nan_is_rejected(self):
        with patch("builtins.input", side_effect=["nan", "10"]):
            self.assertEqual(ask_amount("Amount: "), 10)

if __name__ == "__main__":
    unittest.main()
