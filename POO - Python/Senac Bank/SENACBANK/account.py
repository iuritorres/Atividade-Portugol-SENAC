# Checking Account
class CheckingAccount():
    def __init__(self) -> None:
        self.username = ''
        self.password = ''
        self.accountNumber = 0
        self.checkingBalance = 0

    # Withdraw
    def withdraw(self):
        pass

    # Deposit
    def deposit(self):
        pass

    # Apply
    def apply(self):
        pass

# Savings Account
class SavingsAccount(CheckingAccount):
    def __init__(self) -> None:
        super().__init__()

        self.savingsBalance = 0

    def redeem(self):
        pass