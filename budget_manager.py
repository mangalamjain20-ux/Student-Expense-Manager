def set_budget():
    print("\n--- Set Budget ---")

    budget = float(input("Enter your budget amount: "))

    print("Budget set successfully!")
    print("Budget:", budget)

    return budget


def get_remaining_budget(budget, total_expense):
    return budget - total_expense


def check_budget(budget, total_expense):
    if budget <= 0:
        print("No budget has been set.")
        return

    remaining = get_remaining_budget(budget, total_expense)

    print("Budget:", budget)
    print("Total Expenses:", total_expense)
    print("Remaining Budget:", remaining)

    if total_expense > budget:
        print("Warning: You have exceeded your budget!")
    else:
        print("You are within your budget.")