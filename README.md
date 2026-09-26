# Student Expense Manager

## Overview

Student Expense Manager is a simple Python-based application designed to help students manage and track their daily expenses and budget.

The application allows users to add expenses, view saved expenses, set a budget, search for expenses, and generate a basic expense report.

## Features

* Add new expenses
* View all expenses
* Search expenses by name
* Set a personal budget
* Calculate total expenses
* Display remaining budget
* Show budget warning when expenses exceed the budget
* Save expenses in a CSV file
* Load saved expenses when the program starts
* Validate user input
* Automated testing using Python unittest

## Technologies Used

* Python
* CSV
* Python unittest
* Visual Studio Code
* GitHub

## Project Structure

```text
Student-Expense-Manager/
│
├── Main.py
├── expense_manager.py
├── budget_manager.py
├── reports.py
├── storage.py
├── validation.py
├── utils.py
├── README.md
│
├── data/
│   └── expenses.csv
│
└── tests/
    ├── __init__.py
    └── test_project.py
```

## How to Run

### Step 1: Install Python

Make sure Python is installed on your computer.

Check the Python version using:

```bash
python --version
```

### Step 2: Open the Project

Open the `Student-Expense-Manager` folder in Visual Studio Code.

### Step 3: Run the Application

Open the terminal in the project folder and run:

```bash
python Main.py
```

### Step 4: Use the Menu

The application provides the following options:

1. Add Expense
2. View Expenses
3. Set Budget
4. View Reports
5. Search Expenses
6. Exit

## Data Storage

Expense records are stored in:

```text
data/expenses.csv
```

The application automatically saves expenses to the CSV file and loads them when the program starts.

## Testing

The project contains automated tests using Python's `unittest` framework.

Run the tests using:

```bash
python -m unittest discover -s tests
```

The project currently contains three tests covering:

* Total expense calculation
* Remaining budget calculation
* Empty expense list handling

All three tests should pass successfully.

## Future Enhancements

Some possible future improvements are:

* Add expense date
* Add monthly expense summaries
* Add category-wise reports
* Add graphical charts
* Store budget information permanently
* Add edit and delete expense options
* Add a graphical user interface

## Author

Student Expense Manager Project
