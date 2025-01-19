class BankAccount:
    def __init__(self, balance):
       self.account_balance = balance
       
    def deposit(self, amount):
        self.account_balance += amount
        
    def withdraw(self, amount):
        if amount < 0 or self.account_balance - amount < 0:
            return False
        else:
            self.account_balance -= amount
            
    def display_balance(self):
       print(f"Current Balance: ${self.account_balance:.2f}")
