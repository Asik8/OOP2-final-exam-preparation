class BankAccount():
    def __init__(self,name,balance=0.0):
        self.name = name
        self.balance = balance
        
    def deposite(self,balance):
        if balance >0:
            self.balance+=balance
            print(f"Your New Balance is {self.balance}")
        else:
            print("Enter valid amount")
    
    def withdrawals(self,amount):
        if(amount<=self.balance):
            self.balance -= amount
            print(f"Your New balane after withsrawal is {self.balance}.")
        else:
            print("Not Enough Balance")
            
a1 = BankAccount("Asik",100000)
a1.deposite(10000)
a1.deposite(10000)
a1.deposite(10000)
a1.deposite(10000)

a1.withdrawals(110.11)
