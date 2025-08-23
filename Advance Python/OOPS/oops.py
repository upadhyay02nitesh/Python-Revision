
from abc import ABC, abstractmethod

# -------------------------
# Abstraction
# -------------------------
class Account(ABC):  # Abstract class

    def __init__(self, acc_no, holder_name, balance=0):
        # Encapsulation (private variable)
        self.__balance = balance
        self.acc_no = acc_no
        self.holder_name = holder_name

    # Abstract methods (must be implemented by subclasses)
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    # Concrete methods
    def Bank_Info(self):
        print("Address: 123 Bank St, City Name")

    # Getter for balance (to access private data)
    def get_balance(self):
        return self.__balance

    # Setter (for controlled update of private balance)
    def _set_balance(self, new_balance):   # Protected-like usage
        self.__balance = new_balance


# -------------------------
# Inheritance
# -------------------------
class SavingsAccount(Account):
    
    def deposit(self, amount):
        if amount > 0:
            self._set_balance(self.get_balance() + amount)
            print(f"[Savings] Deposited: {amount}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.get_balance():
            self._set_balance(self.get_balance() - amount)
            print(f"[Savings] Withdrawn: {amount}")
        else:
            print("Insufficient balance in Savings Account")


class CurrentAccount(Account):

    def deposit(self, amount):
        if amount > 0:
            self._set_balance(self.get_balance() + amount)
            print(f"[Current] Deposited: {amount}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        # Current account allows overdraft up to -5000
        if self.get_balance() - amount >= -5000:
            self._set_balance(self.get_balance() - amount)
            print(f"[Current] Withdrawn: {amount}")
        else:
            print("Overdraft limit exceeded in Current Account")


# -------------------------
# Polymorphism
# -------------------------
def transaction(account: Account):
    # Same method name behaves differently based on object type
    account.deposit(1000)
    account.withdraw(500)


# -------------------------
# Usage
# -------------------------
if __name__ == "__main__":
    # Object creation
    sav_acc = SavingsAccount(101, "Alice", 2000)
    cur_acc = CurrentAccount(102, "Bob", 500)

    # Transaction (polymorphism in action)
    print("\n--- Savings Account Transaction ---")
    transaction(sav_acc)
    print("Final Balance:", sav_acc.get_balance())
    print("Account Holder:", sav_acc.holder_name)
    sav_acc.Bank_Info()

    print("\n--- Current Account Transaction ---")
    transaction(cur_acc)
    print("Final Balance:", cur_acc.get_balance())
    print("Account Holder:", cur_acc.holder_name)
    cur_acc.Bank_Info()


# ✅ OOP Concepts Demonstrated

# Class & Object → SavingsAccount, CurrentAccount, sav_acc, cur_acc.

# Encapsulation → __balance private variable + getter/setter.

# Abstraction → Account abstract class + abstract methods.

# Inheritance → SavingsAccount & CurrentAccount inherit Account.

# Polymorphism → transaction() works for both account types differently.