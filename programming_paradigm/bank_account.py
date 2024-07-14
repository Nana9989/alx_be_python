class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance

    def deposit(self, amount):
        #amount = float(input("How much would you like to add today: "))
        self.account_balance +=amount
        return self.account_balance
    def withdrawl(self, amount):
        #amount = float(input("How much would you like to withdraw today"))
        if self.account_balance >= amount:
            return True
        else:
            return False
    def display_balance(self):
        print(f"The current balance is: $")


