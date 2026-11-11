"""Debt Collector - a simple tool to track money people owe you."""

import json
import math
import os

DATA_FILE = "debts.json"


def load_debts():
    """Read the saved debts from the file (empty list if there is no file)."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE) as file:
        return json.load(file)


def save_debts(debts):
    """Write the debts to the file."""
    with open(DATA_FILE, "w") as file:
        json.dump(debts, file, indent=2)


def add_debt(debts, name, amount):
    """Add a new debt to the list."""
    debt = {"name": name, "amount": amount, "paid": 0}
    debts.append(debt)
    return debt


def balance(debt):
    """How much this person still owes."""
    return debt["amount"] - debt["paid"]


def record_payment(debts, name, amount):
    """Add a payment to a person's debt. Returns False if the name is not found."""
    for debt in debts:
        if debt["name"] == name:
            debt["paid"] += amount
            return True
    return False


def total_owed(debts):
    """How much money is still waiting to be collected."""
    return sum(balance(debt) for debt in debts)

def ask_amount(prompt):
    """Keep asking until the user types a number greater than zero."""
    while True:
        text = input(prompt)
        try:
            amount = float(text)
        except ValueError:
            print("Please enter a number, for example 100 or 49.50.")
            continue
        if not math.isfinite(amount) or amount <= 0:
            print("The amount must be greater than zero.")
            continue
        return amount

def show_debts(debts):
    """Print every debt."""
    if not debts:
        print("No debts yet.")
        return
    for debt in debts:
        print(f"{debt['name']}: owes {balance(debt)} (of {debt['amount']})")
    print(f"Total owed: {total_owed(debts)}")


def main():
    debts = load_debts()
    while True:
        print("\n1. Add debt  2. Show debts  3. Record payment  0. Exit")
        choice = input("Choose: ")

        if choice == "1":
            name = input("Name: ")
            amount = ask_amount("Amount owed: ")
            add_debt(debts, name, amount)
            save_debts(debts)
            print("Saved.")
        elif choice == "2":
            show_debts(debts)
        elif choice == "3":
            name = input("Name: ")
            amount = ask_amount("Payment amount: ")
            if record_payment(debts, name, amount):
                save_debts(debts)
                print("Payment recorded.")
            else:
                print("No debt found for that name.")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
