def calculate_total_expenses(expenses):
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    return total


def show_report(expenses, budget):
    print("\n--- Expense Report ---")

    if len(expenses) == 0:
        print("No expenses available for report.")
        return

    total_expense = calculate_total_expenses(expenses)

    print("Total Expenses:", total_expense)
    print("Budget:", budget)

    if budget > 0:
        remaining = budget - total_expense

        print("Remaining Budget:", remaining)

        if total_expense > budget:
            print("Warning: You have exceeded your budget!")
        else:
            print("You are within your budget.")