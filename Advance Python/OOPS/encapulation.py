# Encapsulation is an OOP (Object-Oriented Programming) concept that restricts direct access to some attributes and methods of a class.

# It hides the internal details of how an object works.

# Only exposes a controlled interface for interacting with the object.

# Think of it as a capsule that contains data and methods safely — you can only access them the way the designer intended.



# How Python Implements Encapsulation

# Python uses naming conventions to indicate the level of access:

# Access Level	Syntax	Meaning / Use
# Public	x	Can be accessed from anywhere
# Protected	_x	Should not be accessed outside class (convention)
# Private	__x	Name-mangled to prevent direct access from outside


class BankAccount:
    def __init__(self, balance, account_type):
        self.__balance = balance      # Private variable
        self._account_type = account_type  # Protected variable
        self.bank="SBI"

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount")

    # Withdraw method
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance or invalid amount")

    # Getter for private variable
    def get_balance(self):
        return self.__balance

    # Getter for protected variable (optional)
    def get_account_type(self):
        return self._account_type

# Using the class
account = BankAccount(1000, "Savings")

# Accessing protected variable (possible but by convention should not)
print("Account Type (protected):", account._account_type)

# Accessing via getter
print("Account Type via getter:", account.get_account_type())

# Deposit and withdraw operations
account.deposit(500)
account.withdraw(300)
print("Balance:", account.get_balance())  # 1200

print(account.bank)  # Public variable, accessible directly
print("Account Type (protected):", account._account_type)

# Trying to access private variable directly (will fail)
print(account.__balance)  # ❌ AttributeError


# Trying to access private variable directly
# print(account.__balance)    # ❌ AttributeError
