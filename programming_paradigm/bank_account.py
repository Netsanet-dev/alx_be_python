class BankAccount:
    # current_balance = 0
    def __init__(self, account_balance):
       self.account_balance = account_balance

    def deposit(self, amount):
        current_balance = self.account_balance + amount
        self.account_balance = current_balance
        return self.account_balance
    
    def withdraw(self, amount):
        current_balance = self.account_balance - amount
        self.account_balance = current_balance
        return self.account_balance
    
    
    def display_balance(self):
       current_balance = self.account_balance
       print(f"Current Balance: ${current_balance}")

