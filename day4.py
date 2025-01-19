class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def __str__(self):
        return f"Your account balance is: {self.balance}"

    def __repr__(self):
        return f"BankAccount({self.balance})"
    print(BankAccount(1000))