class BankAccount:
    def __init__(self, balance):
       self.account_balance = balance
       
    def deposit(self, amount):
        self.account_balance += amount

        
    def withdraw(self, amount):
        if self.account_balance - amount <= 0:
            return False
        else:
            self.account_balance -= amount
            
    def display_balance(self):
       print(f"Current Balance: ${self.account_balance}")


if __name__ == "__main__":
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