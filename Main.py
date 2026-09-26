from expense_manager import add_expense, view_expenses, search_expenses
from budget_manager import set_budget, check_budget
from reports import show_report, calculate_total_expenses
from storage import save_expenses, load_expenses
from validation import get_valid_amount, get_valid_budget, get_non_empty_input
from utils import show_menu


def add_new_expense(expenses):
    print("\n--- Add Expense ---")

    expense_name = get_non_empty_input("Enter expense name: ")
    amount = get_valid_amount()
    category = get_non_empty_input("Enter category: ")

    expense = {
        "name": expense_name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("\nExpense added successfully!")
    print("Name:", expense_name)
    print("Amount:", amount)
    print("Category:", category)


def main():
    expenses = load_expenses()
    budget = 0

    print("Welcome to Student Expense Manager!")

    while True:
        show_menu()

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_new_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            budget = get_valid_budget()
            print("Budget set successfully!")
            print("Budget:", budget)

        elif choice == "4":
            show_report(expenses, budget)

        elif choice == "5":
            search_expenses(expenses)

        elif choice == "6":
            save_expenses(expenses)
            print("Thank you for using Student Expense Manager!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()