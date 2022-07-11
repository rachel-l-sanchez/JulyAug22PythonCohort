
class BankAccount:
    def __init__(self, int_rate=0.02, balance=0): 
        self.int_rate = int_rate
        self.balance = balance
        
    def __repr__(self) -> str:
        return f"{self.int_rate}, {self.balance}"            

    def deposit(self, amount):
        self.balance += amount
        return self
    

    def withdraw(self, amount):
        self.balance -= amount
        fee = 10
        if self.balance < 0: 
            self.balance = self.balance - fee
            print("Insufficient funds: Charging a $5 fee")
        return self
     
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    

    def yield_interest(self):
        self.balance = (self.balance * self.int_rate * 12) + self.balance
        return self

rachel = BankAccount(.02, 100000)
elizabeth = BankAccount(.02, 5000)
elizabeth.deposit(10000).withdraw(50).yield_interest().display_account_info()
rachel.deposit(5000).withdraw(100000).display_account_info()
print("rachel-->", rachel)

