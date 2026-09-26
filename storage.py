import csv
import os


DATA_FILE = "data/expenses.csv"


def save_expenses(expenses):
    os.makedirs("data", exist_ok=True)

    with open(DATA_FILE, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["name", "amount", "category"]
        )

        writer.writeheader()
        writer.writerows(expenses)


def load_expenses():
    expenses = []

    if not os.path.exists(DATA_FILE):
        return expenses

    with open(DATA_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            expenses.append({
                "name": row["name"],
                "amount": float(row["amount"]),
                "category": row["category"]
            })

    return expenses