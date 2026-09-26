# Student Expense Manager

## Overview

Student Expense Manager is a Python-based command-line application designed to help students manage their daily expenses and budget.

The project allows users to add and view expenses, set a budget, search for expenses, generate expense reports, validate input, and store expense data in a CSV file.

## Features

* Add new expenses
* View all saved expenses
* Search expenses by name
* Set a student budget
* Calculate total expenses
* Show remaining budget
* Display a warning when the budget is exceeded
* Validate user input
* Store expense data in a CSV file
* Automated testing using Python unittest

## Technologies

* Python 3
* CSV file handling
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
├── data/
│   └── expenses.csv
├── tests/
│   ├── test_project.py
│   └── __init__.py
├── README.md
└── statement.md
```

## Setup and Installation

### 1. Environment Setup

Install Python 3.x on your computer.

To check whether Python is installed, open Command Prompt or PowerShell and run:

```text
python --version
```

The project was developed and tested using Python 3.

### 2. Get the Project

Download or clone the GitHub repository to your computer.

Open the project folder in Visual Studio Code or another Python-supported editor.

### 3. Dependency Installation

This project uses only Python standard library modules.

No external Python packages are required, so there is no `pip install` command needed.

### 4. Configuration

No additional configuration or API keys are required.

The application automatically uses the `data/expenses.csv` file for storing expense information.

### 5. Run the Project

Open a terminal in the project folder and run:

```text
python Main.py
```

The main menu will appear in the terminal.

## How to Use

After starting the program, the user can select:

1. Add Expense
2. View Expenses
3. Set Budget
4. View Reports
5. Search Expenses
6. Exit

Follow the instructions displayed in the terminal.

## Testing

The project includes unit tests using Python's built-in `unittest` framework.

To run the tests:

```text
python -m unittest discover -s tests
```

Expected result:

```text
Ran 3 tests
OK
```

## Future Enhancements

* Monthly expense summaries
* Category-wise expense analysis
* Graphical user interface
* Export reports to PDF
* More advanced filtering options
* Improved budget tracking

## Project Statement

The detailed problem statement, scope, target users, and high-level features are available in `statement.md`.

## Author

Student Expense Manager Project
