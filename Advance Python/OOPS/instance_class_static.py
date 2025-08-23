# 🎯 Summary in Simple Words:

# Instance Method → depends on the object’s own data.
# (👉 Each customer’s bank balance).

# Class Method → depends on class-level data.
# (👉 Common interest rate for all customers).

# Static Method → helper/utility function that doesn’t need object or class.
# (👉 Validate input like deposit amount).


class BankAccount:
    interest_rate = 5   # class variable

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    # Instance method → works with individual accounts
    def deposit(self, amount):
        if BankAccount.validate_amount(amount):   # using static method
            self.balance += amount
            print(f"{self.owner} deposited {amount}, Balance = {self.balance}")
        else:
            print("Invalid deposit amount!")

    # Class method → works with all accounts
    @classmethod
    def set_interest_rate(cls, rate):
        cls.interest_rate = rate
        print(f"Interest rate set to {cls.interest_rate}%")

    # Static method → utility function
    @staticmethod
    def validate_amount(amount):
        return amount > 0


# ---------------- Usage ----------------
acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob", 500)

# Instance method
acc1.deposit(200)         # Alice deposited 200
acc2.deposit(-50)         # Invalid deposit amount!

# Class method
BankAccount.set_interest_rate(6)  # changes for ALL accounts

# Static method
print(BankAccount.validate_amount(300))   # True
