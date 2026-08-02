class BankAccount:
    def __init__(self, account_number, customer_name, date_of_opening, balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.date_of_opening = date_of_opening
        self.balance = balance


    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdrawn:", amount)
        else:
            print("Not enough balance!")

    def check_balance(self):
        print("Current Balance:", self.balance)



account = BankAccount(
    "123456789",
    "Nahian",
    "02-08-2026",
    5000
)

# Test the methods
account.check_balance()

account.deposit(2000)
account.check_balance()

account.withdraw(1500)
account.check_balance()

account.withdraw(7000)