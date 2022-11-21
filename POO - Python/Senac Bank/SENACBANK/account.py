from data_manager import DataManager

BD = DataManager

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
            #Adding current balance with new valueAdding current balance with new value
            self.checkingBalance += value
            #Update checking Balance from currente user
            BD.setUpdateUserProperty(str(self.accountNumber), 'checkingBalance', self.checkingBalance )

            
        elif operator == '-' :
            #Subtracting current balance with new value
            self.checkingBalance -= value
            #Update checking Balance from currente user
            BD.setUpdateUserProperty(str(self.accountNumber), 'checkingBalance', self.checkingBalance )
            
        else:
            print('Operador inválido.')
        

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
            BD.setUpdateUserProperty(str(self.accountNumber), 'savingsBalance', self.savingsBalance)
            
        elif operator == '-' :
            self.savingsBalance -= value
            BD.setUpdateUserProperty(str(self.accountNumber), 'savingsBalance', self.savingsBalance)
        
        else:
            print('Operador inválido.')
            
    # Redeem
    def redeem(self):
        pass