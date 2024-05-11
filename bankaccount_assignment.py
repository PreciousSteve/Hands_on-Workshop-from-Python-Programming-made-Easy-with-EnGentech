# Define a class BankAccount representing a bank account. Implement methods for deposit,
# withdrawal, and balance inquiry.
class BankAccount:
    def __init__(self, account_number, account_name, initial_balance=0):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = initial_balance

    def deposit(self, amount_deposited):
        if amount_deposited > 0:
            self.balance += amount_deposited
            return f"Deposit Successful! You deposited N{amount_deposited}, New balance is N{self.balance}"

    def __str__(self):
        return f"Account number: {self.account_number} with name: {self.account_name} has a balance of N{self.balance}"

    def withdrawal(self, amount_withdrawn):
        if amount_withdrawn > 0:
            self.balance -= amount_withdrawn
            return f"Withdrawal Successful! You withdrawn N{amount_withdrawn}, New balance is N{self.balance}"

    def balance_inquiry(self):
        return f"Dear Customer your CURRENT balance is N{self.balance}"


# creating object
account1 = BankAccount("23400088", "Sally Peters", 1500)

print(account1.deposit(500))
print(account1)
print(account1.withdrawal(1200))
print(account1.balance_inquiry())

account2 = BankAccount("23456788", "Stanley Okoro", 1000)
print(account2.deposit(500))
print(account2)
print(account2.withdrawal(300))
print(account2.balance_inquiry())


# Create a subclass SavingsAccount inheriting from BankAccount. Implement interest
# calculation for savings accounts.
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_name, rate, time, initial_balance=0):
        super().__init__(account_number, account_name, initial_balance=0)
        self.rate = rate
        self.time = time
        self.balance = initial_balance

    def interest(self):
        return (self.balance * self.rate * self.time) / 100


    def __str__(self):
        return (f"Dear Customer, {self.account_name} with account number: {self.account_number} having an initial "
                f"balance of N{self.balance:.2f}\nYou have a interest of N{self.interest():.2f}.\nCURRENT BA"
                f"LANCE = N{self.balance + self.interest():.2f}")


account3 = SavingsAccount("23356667", "Samson okon", 15, 1, 2000)

print(account3.interest())
print(account3)

