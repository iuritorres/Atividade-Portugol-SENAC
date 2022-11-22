# imports
import os
import sys
from time import sleep
from random import randint

from system_tools import Tools
from data_manager import DataManager
from account import CheckingAccount, SavingsAccount

# Instances
tools = Tools
database = DataManager


class BankSystem:

    ## Starts System
    def init(loggedStatus = False):

        # LOGGED OFF MENU
        if loggedStatus == False:
            os.system('cls')

            while True:
                # Initial Form
                options = ['Login', 'Criar Conta', 'Depositar','Sair']
                newLine =  '\n' + f"{'|':<51}" + f"{'|':>}"

                tools.divider()
                print(f"{'| Bem vindo ao Senac Bank!':<50} {'|':>}")
                print(f"{'| O que deseja fazer?:':<50} {'|':>} {newLine}")
                
                for i in range(len(options)): print(f"| {i+1} -> {options[i]:<43} {'|':>}")
                tools.divider()

                # Validate Options
                chosenOption = str(input('\n-> Escolha uma opção: '))
                
                # Login Option
                if chosenOption == '1':

                    # Login Validation
                    while True:

                        tools.showMessage('Entrar em uma conta existente:')
                        idLogin = str(input('Informe o ID da conta: '))

                        try:
                            passwordLogin = int(input('Informe a senha da conta: '))
                            user = database.getUser(idLogin)

                            if type(user) == dict:

                                if passwordLogin == user.get('password'):
                                    tools.validateTimer('Validando')

                                    logUserName = user.get('username')
                                    logUserPassword = user.get('password')
                                    logUserID = idLogin
                                    logUserCheckingBalance = user.get('checkingBalance')
                                    logUserSavingsBalance = user.get('savingsBalance')

                                    global loggedUser
                                    loggedUser = SavingsAccount(logUserName, logUserPassword, logUserID, logUserCheckingBalance, logUserSavingsBalance)

                                    # Change Logged Status
                                    BankSystem.init(True)

                                else:
                                    tools.validateTimer('Validando')
                                    tools.showMessage('Usuario inexistente ou senha incorreta')
                                    sleep(2)
                                
                            if type(user) == str:
                                tools.validateTimer('Validando')
                                tools.showMessage('Usuario inexistente ou senha incorreta')
                                sleep(2)


                        except ValueError:
                            tools.validateTimer('Validando')
                            tools.showMessage('A senha permite apenas números, tente novamente.')
                            sleep(2)


                # Create Account
                elif chosenOption == '2':

                    tools.showMessage('Criando uma nova conta:')

                    # ID and username
                    id = randint(100, 999)
                    name = str(input('Digite seu nome completo: ')).title()

                    # Password
                    while True:
                        try:
                            tools.showMessage('Criando uma nova conta:')
                            print(f'-> Nome: {name}\n')

                            password = int(input('Digite sua senha (4 dígitos numéricos): '))
                            tools.showMessage('Criando uma nova conta:')
                            print(f'-> Nome: {name}')
                            print(f'-> Senha: {password}\n')

                            if len(str(password)) != 4:
                                tools.showMessage('Sua senha não tem 4 dígitos')
                                print(f'-> Nome: {name}\n')
                                sleep(2)
                            else:
                                break

                        except ValueError:
                            tools.showMessage('Sua senha só pode conter números')
                            print(f'-> Nome: {name}\n')
                            sleep(2)

                    # First deposit
                    while True:
                        try:
                            firstDepositValue = int(input('Faça um deposito inicial: R$'))

                            if firstDepositValue <= 0:
                                print('Para depositar, insira um valor maior que zero.')
                            else:
                                break
                        
                        except ValueError:
                            tools.showMessage('Valor inválido')
                            print(f'-> Nome: {name}')
                            print(f'-> Senha: {password}\n')

                    # Add user to data base
                    newUser = {
                        "username": name,
                        "password": password,
                        "checkingBalance": firstDepositValue,
                        "savingsBalance": 0
                    }
                    
                    database.setUser(id, newUser)
                    tools.validateTimer('Criando a conta')

                    # Success in account create
                    mensagem = 'Conta criada com sucesso!'
                    
                    tools.showMessage(mensagem)
                    sleep(2)

                    BankSystem.showData(id)
                    sleep(1)
                    os.system('cls')

                # Deposit
                elif chosenOption == '3':
                    pass

                # Exit System
                elif chosenOption == '4':
                    BankSystem.exit()
                    
                # Not existing function
                else:
                    tools.showMessage('Digite uma opção válida!')


        # LOGGED IN MENU
        if loggedStatus == True:
            os.system('cls')

            while True:
                # Welcome of login

                firstName = f"Bem vindo {database.getUser(loggedUser.__getattribute__('accountNumber'))['username'].split(' ')[0]}"

                tools.showMessage(firstName)

                # Initial Logged Menu Form
                options = ['Sacar', 'Depositar', 'Aplicar', 'Resgatar', 'Mostrar Dados', 'Sair']
                newLine =  '\n' + f"{'|':<51}" + f"{'|':>}"

                tools.divider()
                print(f"{'| Bem vindo ao Senac Bank!':<50} {'|':>}")
                print(f"{'| O que deseja fazer?:':<50} {'|':>} {newLine}")
                
                for i in range(len(options)): print(f"| {i+1} -> {options[i]:<43} {'|':>}")
                tools.divider()

                # Validate Options
                chosenOption = str(input('\n-> Escolha uma opção: '))

                # Withdraw
                if chosenOption == '1':
                    
                    # User input
                    while True:
                        try:
                            currentChekingBalance = loggedUser.getCheckingBalance()

                            tools.showMessage('Saque:')
                            withdrawValue = int(input('Digite 0 para cancelar a operação.\n\n-> Insira o valor que deseja retirar: R$'))
                            
                            if withdrawValue == 0:
                                tools.showMessage('Operação cancelada!')
                                sleep(2)
                                break
                            
                            elif withdrawValue < 0:
                                tools.showMessage('Por favor, insira um valor maior que zero.')
                                sleep(2)

                            elif withdrawValue > currentChekingBalance:
                                tools.showMessage('Saldo insuficiente!')
                                sleep(2)

                            else:
                                # Setting new value   
                                loggedUser.setCheckingBalance('-', withdrawValue)
                                
                                tools.validateTimer('Sacando')
                                tools.showMessage('O saque realizado com sucesso!', f'Seu saldo atual é R$ {loggedUser.getCheckingBalance()}')
                                sleep(3)
                                break
                            
                        except ValueError:
                            tools.showMessage('Por favor, insira um número válido.')
                            sleep(2)
                
                # Deposit
                elif chosenOption == '2':

                    # User input
                    while True:
                        try:
                            tools.showMessage('Depósito:')
                            depositValue = int(input('Digite 0 para cancelar a operação.\n\n-> Insira o valor que deseja depositar: R$'))
                            
                            if depositValue == 0:
                                tools.showMessage('Operação cancelada!')
                                sleep(2)
                                break
                            
                            elif depositValue < 0:
                                tools.showMessage('Por favor, insira um valor maior que zero.')
                                sleep(2)

                            else:
                                loggedUser.setCheckingBalance('+', depositValue)

                                tools.validateTimer('Depositando')
                                tools.showMessage('O dinheiro foi depositado!', f'Seu saldo atual é R$ {loggedUser.getCheckingBalance()}')
                                sleep(3)
                                break
                            
                        except ValueError:
                            tools.showMessage('Por favor, insira um número válido.')
                            sleep(2)
                
                # Apply
                elif chosenOption == '3':
                    
                    while True:
                        try:
                            tools.showMessage('Aplicar:')
                            applyValue = int(input('Digite 0 para cancelar a operação.\n\n-> Insira o valor que deseja transferir: R$'))
                            
                            if applyValue == 0:
                                tools.showMessage('Operação cancelada!')
                                sleep(2)
                                break
                            
                            elif applyValue < 0:
                                tools.showMessage('Por favor, insira um valor maior que zero.')
                                sleep(2)

                            else:
                                # Getting current checking balance and setting a new one   
                                currentCheckingBalance = loggedUser.getCheckingBalance()

                                if currentCheckingBalance >= applyValue:

                                    loggedUser.setCheckingBalance('-', applyValue)
                                    loggedUser.setSavingsBalance('+', applyValue)
                                    

                                    tools.validateTimer('Transferindo')
                                    tools.showMessage('O dinheiro foi transferido com sucesso!')
                                    sleep(3)
                                    break

                                else:
                                    tools.showMessage('Você não possui saldo suficiente')
                                    sleep(2)
                            
                        except ValueError:
                            tools.showMessage('Por favor, insira um número válido.')
                            sleep(2)

                # Redeem
                elif chosenOption == '4':
                    while True:
                        try:
                            tools.showMessage('Resgatar:')
                            redeemValue = (int(input('Digite 0 para cancelar a operação.\n\n -> Insira o valor que deseja resgatar: R$')))
                            
                            if redeemValue == 0:
                                tools.showMessage('Operação cancelada!')
                                sleep(2)
                                break

                            elif redeemValue < 0:
                                tools.showMessage('Por favor, digite um valor acima de zero')
                                sleep(2)

                            else:
                                # Getting current savings balanceand setting a new one 
                                currentSavingsBalance = loggedUser.getSavingsBalance()

                                if currentSavingsBalance >= redeemValue:
                                    loggedUser.setSavingsBalance('-', redeemValue)
                                    loggedUser.setCheckingBalance('+',redeemValue)

                                    tools.validateTimer('Transferindo')
                                    tools.showMessage('O dinheiro foi resgatado com sucesso!')
                                    sleep(3)
                                    break
                                    
                                else:
                                    tools.showMessage('Você não possui saldo suficiente')
                                    sleep(2)

                        except ValueError:
                            tools.showMessage('Por favor, insira um número válido.')
                            sleep(2)

                # Show Data
                elif chosenOption == '5':
                    BankSystem.showData(loggedUser.__getattribute__('accountNumber'))

                # Exit System
                elif chosenOption == '6':
                    BankSystem.exit()

                # Not existing function
                else:
                    tools.showMessage('Digite uma opção válida!')

    # Show Account Data
    def showData(userID):
        os.system('cls') # Clear Console

        userData = database.getUser(userID)

        back = '-> Aperte "Enter" para voltar...'
        newLine =  '\n' + f"{'|':<51}" + f"{'|':>}"
        printAccountNumber = f'-> Número da conta: {userID}'

        user_keys = ['Nome', 'Senha', 'Saldo conta corrente', 'Saldo conta poupança' ]
        user_values = list(userData.values())

        tools.divider()

        print(f"{'|':<} {'Seus Dados:':^48} {'|':>} {newLine}")

        print(f'|{printAccountNumber:<50}|')
        for i in range(len(user_keys)):
            user_data = f'-> {user_keys[i]}: {user_values[i]}'

            print(f'|{user_data:<50}|')

        tools.divider()

        backToMenu = input(f'{back:<50}')

        if backToMenu != None:
            return True

    ## Quit system
    def exit():        
        tools.showMessage('Você escolheu a opção sair...')

        sleep(1)
        os.system('cls')
        
        # Timer to end
        for i in range(3, 0, -1):
            os.system('cls')
            tools.divider()
            print(f"{'|':<} {'Você escolheu a opção sair...':^48} {'|':>}")
            print(f"{'|':<} {'Sistema finalizando em {} segundos':^49} {'|':>}".format(i))
            tools.divider()
            sleep(1)

        # End System
        os.system('cls')
        sys.exit()

