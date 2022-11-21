# imports
import os
import sys
from time import sleep
from random import randint

from system_tools import Tools
from data_manager import DataManager
from account import CheckingAccount, SavingsAccount

# instances
tools = Tools
database = DataManager


class BankSystem:

    ## Starts System
    def init(loggedStatus = False):
        os.system('cls') # clear console

        # LOGGED OFF MENU
        if loggedStatus == False:

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
                        
                        idLogin = str(input('Informe o ID da conta: '))
                        passwordLogin = input('Informe a senha da conta: ')
                        userDB = database.getUser(idLogin)
                        
                        if type(userDB) == object:
                            print(userDB)
                            
                        else:
                            print(userDB)
                        

                # Create Account
                elif chosenOption == '2':

                    id = randint(100, 999)
                    name = str(input('Digite seu nome completo: ')).title()

                    # password
                    while True:
                        try:
                            password = int(input('Digite sua senha (4 digitos numericos): '))

                            if len(str(password)) != 4:
                                print('Sua senha nao tem 4 digitos')
                            else:
                                break

                        except ValueError:
                            print('Sua senha so pode conter numeros')

                    # first deposit
                    while True:
                        try:
                            firstDepositValue = int(input('Faca um deposito inicial: R$'))

                            if firstDepositValue <= 0:
                                print('Para depositar, insira um valor maior que zero.')
                            else:
                                break
                        
                        except ValueError:
                            print('Valor invalido')

                    # add user to data base
                    newUser = {
                        "username": name,
                        "password": password,
                        "checkingBalance": firstDepositValue,
                        "savingsBalance": 0
                    }
                    
                    database.setUser(id, newUser)

                    # success in account create
                    mensagem = 'Conta criada com sucesso!'
                    
                    os.system('cls')
                    print('+'+'-'*50+'+')
                    print(f"|{mensagem:^50}|")
                    print('+'+'-'*50+'+')
                    sleep(3)

                    BankSystem.showData(id)
                    sleep(5)

                # Deposit
                elif chosenOption == '3':
                    pass

                # Exit System
                elif chosenOption == '4':
                    BankSystem.exit()
                    
                # Not existing function
                else:
                    os.system('cls')
                    tools.divider()
                    print(f"{'|':<} {'Digite uma opção válida!':^48} {'|':>}")
                    tools.divider()


        # LOGGED IN MENU
        if loggedStatus == True:
            
            while True:
                # Welcome of login
                firstName = 'Bem vindo ' #+ BD.getUser()[userIndex]['owner'].split(' ')[0]

                print('+'+'-'*50+'+')
                print(f'|{firstName:^50}|')
                print('+'+'-'*50+'+')

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
                    
                    while True:
                        try:
                            withdrawValue = int(input('Insira o valor que deseja retirar (Digite 0 para cancelar a operação.): R$'))
                            
                            if withdrawValue == 0:
                                break
                            
                            elif withdrawValue < 0:
                                print('Digite um número válido para a operação.')
                            
                        except ValueError:
                            print('É permitido apenas números no campo de valor.')
                            
                        
                        finally:
                        # Get and Set CheckingAccount here
                            pass
                
                # Deposit
                elif chosenOption == '2':
                    pass
                
                # Apply
                elif chosenOption == '3':
                    pass

                # Redeem
                elif chosenOption == '4':
                    pass

                # Show Data
                elif chosenOption == '5':
                    pass

                # Exit System
                elif chosenOption == '6':
                    BankSystem.exit()

                # Not existing function
                else:
                    os.system('cls')
                    tools.divider()
                    print(f"{'|':<} {'Digite uma opção válida!':^48} {'|':>}")
                    tools.divider()

    # Show Account Data
    def showData(userID):
        userData = database.getUser(userID)

        newLine =  '\n' + f"{'|':<51}" + f"{'|':>}"

        user_keys = list(userData.keys())
        user_values = list(userData.values())

        tools.divider()
        print(f"{'|':<} {'Seus Dados:':^48} {'|':>} {newLine}")

        for i in range(len(user_keys)):
            user_data = f'-> {user_keys[i]}: {user_values[i]}'

            print(f'|{user_data:<50}|')

        tools.divider()

    ## Quit system
    def exit():
        os.system('cls') # clear console
        tools.divider()
        print(f"{'|':<} {'Você escolheu a opção sair...':^48} {'|':>}")
        tools.divider()

        sleep(1)
        os.system('cls')
        
        # timer to end
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

