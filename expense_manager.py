def add_expense(expenses):
    print("\n--- Add Expense ---")

    expense_name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    expense = {
        "name": expense_name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)

    print("\nExpense added successfully!")
    print("Name:", expense_name)
    print("Amount:", amount)
    print("Category:", category)


def view_expenses(expenses):
    print("\n--- All Expenses ---")

    if len(expenses) == 0:
        print("No expenses found.")
        return

    for expense in expenses:
        print("Name:", expense["name"])
        print("Amount:", expense["amount"])
        print("Category:", expense["category"])
        print("--------------------")


def search_expenses(expenses):
    print("\n--- Search Expenses ---")

    search_name = input("Enter expense name to search: ")

    found = False

    for expense in expenses:
        if search_name.lower() in expense["name"].lower():
            print("\nExpense Found!")
            print("Name:", expense["name"])
            print("Amount:", expense["amount"])
            print("Category:", expense["category"])
            print("--------------------")
            found = True

    if found == False:
        print("No matching expense found.")