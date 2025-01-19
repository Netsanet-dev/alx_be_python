class BankAccount:
    account_balance = 0
    def __init__(self, account_balance):
       self.account_balance = account_balance
       
    def deposit(self, amount):
        BankAccount.account_balance = self.account_balance + amount
        print(f"{BankAccount.account_balance} deposited")
        return self.account_balance
    
    def withdraw(self, amount):
        BankAccount.account_balance = self.account_balance - amount
        print(f"{self.account_balance} deposited")
        return self.account_balance
    
    def display_balance(self):
       print(f"Current Balance: ${BankAccount.account_balance}")
       
       
# if __name__ == "__main__":
#     import sys
#     from bank_account import BankAccount
#     while True:
#         command = input("command: ")
#         amount = int(input("number: "))
#         account = BankAccount(100)  # Example starting balance
#         if command == "deposit" and amount is not None:
#             account.deposit(amount)
#             print(f"Deposited: ${amount}")
#         elif command == "withdraw" and amount is not None:
#             if account.withdraw(amount):
#                 print(f"Withdrew: ${amount}")
#             else:
#                 print("Insufficient funds.")
#         elif command == "display":
#             account.display_balance()
#         elif command == 'q':
#             break
