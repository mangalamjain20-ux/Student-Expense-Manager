def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
            else:
                return amount

        except ValueError:
            print("Please enter a valid number.")


def get_valid_budget():
    while True:
        try:
            budget = float(input("Enter your budget amount: "))

            if budget < 0:
                print("Budget cannot be negative.")
            else:
                return budget

        except ValueError:
            print("Please enter a valid number.")


def get_non_empty_input(message):
    while True:
        value = input(message).strip()

        if value:
            return value

        print("This field cannot be empty.")