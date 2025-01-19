class BankAccount:
    balance = 0
    def __init__(self, account_balance):
       self.account_balance = account_balance
       
    def deposit(self, amount):
        BankAccount.balance = self.account_balance + amount
        print(f"{self.account_balance} deposited")
        return self.balance
    
    def withdraw(self, amount):
        BankAccount.balance = self.account_balance - amount
        print(f"{self.account_balance} deposited")
        return self.balance
    
    def display_balance(self):
       print(f"Current Balance: ${self.balance}")
