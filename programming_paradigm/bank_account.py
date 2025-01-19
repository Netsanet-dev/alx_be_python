class BankAccount:
    def __init__(self, balance):
       self.account_balance = balance
       
    def deposit(self, amount):
        self.account_balance += amount
        return self.account_balance
        
    def withdraw(self, amount):
        if amount < 0 or amount > self.account_balance:
            return False
        else:
            self.account_balance -= amount
            return self.account_balance
            
    def display_balance(self):
       print(f"Current Balance: ${self.account_balance:.2f}")
