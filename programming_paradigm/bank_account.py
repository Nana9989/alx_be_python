class BankAccount():
    def __init__(self, account_balance):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance +=amount
        return self.account_balance
    def withdrawl(self, amount):
        if self.account_balance >= amount:
            return True
        else:
            return False
    def display_balance(self):
        print(f"The current balance is: $")


