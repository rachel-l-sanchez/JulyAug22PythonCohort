
class BankAccount:
    def __init__(self, int_rate=0.02, balance=0): 
        self.int_rate = int_rate
        self.balance = balance
        
    def __repr__(self) -> str:
        return f"{self.int_rate}, {self.balance}"            

    # method to add to the existing balance using a deposit amount
    def deposit(self, amount):
        self.balance += amount
        return self
    
    # method to subtract to the existing balance using a withdrawal amount

    def withdraw(self, amount):
        self.balance -= amount
        fee = 10
        if self.balance < 0: 
            self.balance -= fee
            print("Insufficient funds: Charging a $5 fee")
        return self
    
    # method to display current balance
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    
    # method to output compouding interest
    def yield_interest(self):
        self.balance = (self.balance * self.int_rate * 12) + self.balance
        return self
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
        self.other_account = BankAccount(int_rate=0.02, balance = 0)
        self.other_user = BankAccount(int_rate = 0.02, balance = 0)
    
    # allows a user to make a deposit using the deposit method in the BankAccount class
    def make_deposit(self, amount):
        self.amount = self.account.deposit(amount)
        print(self.account.deposit)
        account = input('Which account are you depositing to?')
        if account == self.account:
            self.account.self.balance += amount
        elif account == self.other_account:
            self.other_account.self.balance += amount
        print('{amount} has been added to your account')
        return self  

    # allows a user to make a withdrawal
    # take user input to specify which account to withdraw from
    # transfer the amount specified to the specified account
    def make_withdrawal(self, amount):
        self.amount = self.account.withdraw(amount)
        account = input('Which account are you withdrawing from?')
        if account == self.account:
            self.balance.self.account += amount
        elif account == self.other_account:
            self.other_account.self.balance += amount
        print('{amount} has been withdrawn from your account')
        return self
    
    # method to output the attributes from the constructor init
    def display_info(self):
        self = self.account.display_account_info
        return self

    # method to transfer money from one user to another
    # take user input to specify which account to transfer to
    # use a conditional to confirm account validity
    # transfer the money from self.account to the other account
    def transfer_money(self,amount, other_user):
        user = input("Which user would you like to transfer money to?")
        user_email = input('User Email:')
        user_full_name = input('Full Name:')
        if user_email == self.other_user:
            transfer = self.account.self.balance - self.amount
            self.other_user.balance += transfer

rachel = BankAccount(.02, 100000)
elizabeth = BankAccount(.02, 5000)
elizabeth.deposit(10000).withdraw(50).yield_interest().display_account_info()
rachel.deposit(5000).withdraw(100000).display_account_info()
john = User('John Smith', 'john.smith@gmail.com')
john.transfer_money(30, 'John Smith')
john.make_withdrawal(300).make_deposit(500)
