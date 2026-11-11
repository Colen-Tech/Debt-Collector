"""Tests for main.py. Run with: python -m unittest"""

import unittest

from main import add_debt, balance, record_payment, total_owed


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


if __name__ == "__main__":
    unittest.main()
