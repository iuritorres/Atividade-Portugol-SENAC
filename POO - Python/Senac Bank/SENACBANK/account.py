# Checking Account
class CheckingAccount():
    def __init__(self) -> None:
        self.username = ''
        self.password = ''
        self.accountNumber = 0
        self.checkingBalance = 0
        
    # Get Checking Balance Account
    def getChekingBalance(self):
        return self.checkingBalance
    
    # Set Checking Balance Account
    def setChekingBalance(self, operator, value):
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
    def __init__(self) -> None:
        super().__init__()

        self.savingsBalance = 0
        
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