from Tools import Tools
from BancoDeDados import BancoDeDados
from random import randint
import os
from time import sleep

tools = Tools
BD = BancoDeDados

class Account:
    # Login
    def login(accountNumber, password):
        # Validate user
        i = 0
        while i < len(BD.getUser()):
            dic = BD.getUser()[i]
            userNumber = dic.get('accountNumber')
            userPassword = dic.get('password')
            
            if userNumber == accountNumber:
                # Validate password
                if userPassword == password:
                    global userIndex
                    userIndex = i

                    return True
                
                else:
                    tools.showMensage('Você digitou uma senha invalida!')
                    break
            
            i += 1
            if i == len(BD.getUser()):
                tools.showMensage('Você digitou um usuário invalido(a)!')
                
        
    # Create Account
    def createAccount():
        os.system('cls') # clear console

        # Interface
        tools.divider()
        print(f"|{'Criar conta':^50}|")
        tools.divider()

        ownerCompleteName = str(input('-> Digite seu nome completo: ')).title()

        # Validate existing Account Numbers
        while True:
            newAccountNumber = randint(100, 999)

            i = 0
            while i < len(BD.getUser()):
                dic = BD.getUser()[i] 
                existingNumber = dic.get('accountNumber')

                if newAccountNumber == existingNumber:
                    newAccountNumber = randint(100, 999)
                else:
                    break

                i += 1
                
            break

        # Validate deposit value
        while True:
            initialDeposit = float(input('-> Para continuar, efetue um depósito inicial: R$'))
            if initialDeposit <= 0:

                os.system('cls') # clear console
        
                tools.divider()
                print(f"|{'Digite um valor maior que 0':^50}|")
                tools.divider()
            else:
                break

        # Creating user password
        userPassword = str(input('-> Digite sua senha de acesso: '))

        # Adding user to database
        newUser = {
            'accountNumber': newAccountNumber,
            'owner': ownerCompleteName,
            'balance': initialDeposit,
            'password': userPassword
        }

        BD.setUser(newUser)

        # Warning user
        os.system('cls') # clear console

        accountNumber = 'Conta -> ' + str(newAccountNumber)
        accountOwner = 'Proprietário -> ' + str(ownerCompleteName)
        accountBalance = 'Saldo -> R$' + str(initialDeposit)

        tools.divider()
        print(f"|{'Seus dados são':^50}|")
        tools.divider()
        tools.divider()
        print(f"| {accountNumber:<49}|")
        print(f"| {accountOwner:<49}|")
        print(f"| {accountBalance:<49}|")
        tools.divider()    
        
        sleep(5)
        os.system('cls')

    # Show User data
    def showData():
        while True:
            os.system('cls') # clear console

            accountNumber = 'Conta -> ' + str(BD.getUser()[userIndex].get('accountNumber'))
            accountOwner = 'Proprietário -> ' + str(BD.getUser()[userIndex].get('owner'))
            accountBalance = 'Saldo -> R$' + str(BD.getUser()[userIndex].get('balance'))
            back = '-> Aperte "Enter" para voltar...'

            tools.divider()
            print(f"|{'Seus dados são':^50}|")
            tools.divider()
            tools.divider()
            print(f"| {accountNumber:<49}|")
            print(f"| {accountOwner:<49}|")
            print(f"| {accountBalance:<49}|")
            tools.divider()    
            backToMenu = input(f'{back:<50}')

            if backToMenu != None:
                return True


    # Deposit Cash
    def deposit():
        os.system('cls') # clear console
        while True:

            # Get current balance
            currentBalance = BD.getUser()[userIndex].get('balance')

            # Interface
            currentBalancePrint = ' Saldo Atual -> ' + str(currentBalance)
            tools.divider()
            print(f"|{'Depositar dinheiro':^50}|")
            tools.divider()

            tools.divider()
            print(f"|{currentBalancePrint:<50}|")
            tools.divider()

            # Update account balance
            depositValue = float(input('-> Insira o valor a ser depositado: R$'))

            if depositValue <= 0:
                os.system('cls') # clear console
        
                tools.divider()
                print(f"|{'Digite um valor maior que 0':^50}|")
                tools.divider()
            else:
                currentBalance += depositValue
                BD.getUser()[userIndex]['balance'] = currentBalance

                return True

    # Withdraw Cash
    def withdrawCash():
        os.system('cls') # clear console
        while True:

            # Get current balance
            currentBalance = BD.getUser()[userIndex].get('balance')

            # Interface
            currentBalancePrint = ' Saldo Atual -> ' + str(currentBalance)
            tools.divider()
            print(f"|{'Sacar dinheiro':^50}|")
            tools.divider()

            tools.divider()
            print(f"|{currentBalancePrint:<50}|")
            tools.divider()

            # Update account balance
            withdrawValue = float(input('-> Insira o valor a ser sacado: R$'))

            if withdrawValue > currentBalance:
                os.system('cls') # clear console
        
                tools.divider()
                print(f"|{'Você não tem saldo suficiente! Pobre hahah':^50}|")
                tools.divider()
            else:
                currentBalance -= withdrawValue
                BD.getUser()[userIndex]['balance'] = currentBalance

                return True

    # To see transaction history
    def transactionHistory():
        pass


class AccountPoupansa:
    pass