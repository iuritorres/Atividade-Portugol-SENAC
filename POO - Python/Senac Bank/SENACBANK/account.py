# Checking Account
class CheckingAccount():
    def __init__(self, username, password, accountNumber, checkingBalance) -> None:
        self.username = username
        self.password = password
        self.accountNumber = accountNumber
        self.checkingBalance = checkingBalance

    # Get Checking Balance Account
    def getCheckingBalance(self):
        return self.checkingBalance
    
    # Set Checking Balance Account
    def setCheckingBalance(self, operator, value):
        if operator == '+':
            self.checkingBalance += value
            
        elif operator == '-' :
            self.checkingBalance -= value
            
        else:
            print('Operador inválido.')
        
    
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
    def __init__(self, username, password, accountNumber, checkingBalance, savingsBalance) -> None:
        super().__init__(username, password, accountNumber, checkingBalance)

        self.savingsBalance = savingsBalance
        
        # Get Savings Balance Account
        def getSavingsBalance(self):
            return self.savingsBalance
        
        # Set Saving Balance Account
        def setSavingsBalance(self, operator, value):
            if operator == '+':
                self.savingsBalance += value
            
            elif operator == '-' :
                self.savingsBalance -= value
            
            else:
                print('Operador inválido.')
    # Redeem
    def redeem(self):
        pass