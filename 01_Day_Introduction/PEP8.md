# Python Style Guide: PEP 8

**PEP 8** is Python's **official style guide**.

It stands for **Python Enhancement Proposal 8**, written in 2001 by Python's creator Guido van Rossum, Barry Warsaw, and Nick Coghlan.

Its primary goal is to make Python code as **readable and consistent** as possible across different developers and projects (*"Readability counts"* — The Zen of Python).

---

## Key PEP 8 Guidelines

### 1. Indentation
* Use **4 spaces** per indentation level.
* Do not mix tabs and spaces (Python 3 disallows mixing tabs and spaces for indentation).

### 2. Naming Conventions

| Type | Naming Convention | Example |
| :--- | :--- | :--- |
| **Variables** | `snake_case` (lowercase with underscores) | `first_name`, `user_age` |
| **Functions** | `snake_case` (lowercase with underscores) | `calculate_total()`, `get_data()` |
| **Classes** | `PascalCase` (CapitalizedWords) | `BankAccount`, `UserProfile` |
| **Constants** | `UPPER_CASE_WITH_UNDERSCORES` | `PI`, `MAX_CONNECTIONS` |
| **Modules** | short, lowercase names (underscores optional) | `my_module.py` |
| **Packages** | short, lowercase names (no underscores) | `mypackage` |

```python
# Variables & Functions
first_name = "Asabeneh"

def calculate_total(price, tax_rate):
    return price + (price * tax_rate)

# Class
class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder

# Constant
PI = 3.14159
MAX_RETRIES = 5
```

---

### 3. Spacing and Whitespace

#### Around Operators
Always surround binary operators with a single space on either side:
```python
# Good
x = 5
total = x + 10
is_valid = x > 0 and total < 100

# Avoid
x=5
total=x+10
is_valid=x>0and total<100
```

#### Around Function Arguments & Keyword Parameters
Do not use spaces around the `=` sign when used to indicate a default argument value:
```python
# Good
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"

# Avoid
def greet(name, greeting = "Hello"):
    return f"{greeting}, {name}"
```

#### Inside Parentheses, Brackets, and Braces
Avoid extraneous whitespace immediately inside parentheses, brackets, or braces:
```python
# Good
numbers = [1, 2, 3]
person = {'name': 'Asabeneh'}

# Avoid
numbers = [ 1, 2, 3 ]
person = { 'name': 'Asabeneh' }
```

---

### 4. Imports

* Imports should always be at the top of the file, just after any module comments and docstrings.
* Put each import on a separate line:

```python
# Good
import os
import sys

# Avoid
import os, sys
```

* Order imports in three distinct groups separated by a blank line:
  1. Standard library imports (e.g., `import os`, `import sys`)
  2. Related third-party imports (e.g., `import numpy`, `import pandas`)
  3. Local application/library-specific imports (e.g., `from mymodule import my_function`)

---

### 5. Maximum Line Length & Blank Lines

* **Line Length**: Limit all lines to a maximum of **79 characters** (docstrings/comments to 72). Many modern teams allow 88 or 100 characters, but 79 is the PEP 8 standard.
* **Blank Lines**:
  * Surround top-level function and class definitions with **two blank lines**.
  * Method definitions inside a class are surrounded by a **single blank line**.
  * Use blank lines sparingly inside functions to separate logical sections.

---

### 6. Comments

* Keep comments up-to-date when the code changes.
* Comments should be complete sentences with proper capitalization.
* Inline comments should be separated by at least two spaces from the statement:
```python
x = x + 1  # Increment counter
```

---

## Modern Tools to Automate PEP 8

You do not need to memorize every rule manually. Modern Python development relies on tools to enforce styling:

* **Formatters** (Automatically reformat your code to PEP 8 standard):
  * `black` — The uncompromising Python code formatter.
  * `ruff format` — An extremely fast Python code formatter written in Rust.
* **Linters** (Check code for style violations and potential bugs):
  * `flake8` — A popular tool that enforces PEP 8 and checks for syntax errors.
  * `ruff` — An ultra-fast linter combining flake8, isort, and more.
  * `pylint` — A thorough static code analyzer.
