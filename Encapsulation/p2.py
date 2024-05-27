# 2. Implement a class `BankAccount` with private attributes `__balance`. Provide public methods to deposit, withdraw, and check balance, ensuring that withdrawals cannot exceed the balance.

class BankAccount:
    def __init__(self):
        self.__balance = 0
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")
    
    def check_balance(self):
        return self.__balance
