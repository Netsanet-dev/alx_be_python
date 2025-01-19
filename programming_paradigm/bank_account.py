class BankAccount:
    balance = 0
    def __init__(self, account_balance):
       self.account_balance = account_balance
       
    def deposit(self, amount):
        BankAccount.balance = self.account_balance + amount
        return BankAccount.balance
    
    def withdraw(self, amount):
        if self.account_balance - amount <= 0:
            return False
        else:
            BankAccount.balance = self.account_balance - amount
            return BankAccount.balance
    
    def display_balance(self):
       print(f"Current Balance: ${self.balance}")


if __name__ == "__main__":
    import sys
    from bank_account import BankAccount
    while True:
        command = input("command: ")
        amount = int(input("number: "))
        account = BankAccount(100)  # Example starting balance
        if command == "deposit" and amount is not None:
            account.deposit(amount)
            print(f"Deposited: ${amount}")
        elif command == "withdraw" and amount is not None:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount}")
            else:
                print("Insufficient funds.")
        elif command == "display":
            account.display_balance()
        elif command == 'q':
            break