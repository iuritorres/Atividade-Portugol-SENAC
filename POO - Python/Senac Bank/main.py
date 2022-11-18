# DEVS: IURI TORRES | RAFAEL LUIS #

# imports
import os
import sys
from time import sleep
from Account import Account
from Tools import Tools
from BancoDeDados import BancoDeDados

Account = Account
tools = Tools
BD = BancoDeDados



# Main - SenacBankSystem
class SenacBankSystem:

    ## Starts System
    def init(loggedStatus=False):
        os.system('cls') # clear console

        # Starts System Menu Loop if logged=False
        if loggedStatus == False:
            
            while True:
                # Initial Form
                options = ['Login', 'Criar Conta', 'Sair']
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
                    if SenacBankSystem.login() == True:
                        SenacBankSystem.init(True)
                        break

                # Create Account
                elif chosenOption == '2':
                    Account.createAccount()

                # Exit System
                elif chosenOption == '3':
                    SenacBankSystem.exit()
                    
                # Not existing function
                else:
                    os.system('cls')
                    tools.divider()
                    print(f"{'|':<} {'Digite uma opção válida!':^48} {'|':>}")
                    tools.divider()


        # Starts Logged User Menu
        if loggedStatus == True:

            while True:
                # Welcome of login
                firstName = 'Bem vindo ' #+ BD.getUser()[userIndex]['owner'].split(' ')[0]

                print('+'+'-'*50+'+')
                print(f'|{firstName:^50}|')
                print('+'+'-'*50+'+')

                # Initial Logged Menu Form
                options = ['Mostrar Dados', 'Depositar', 'Sacar', 'Sair']
                newLine =  '\n' + f"{'|':<51}" + f"{'|':>}"

                tools.divider()
                print(f"{'| Bem vindo ao Senac Bank!':<50} {'|':>}")
                print(f"{'| O que deseja fazer?:':<50} {'|':>} {newLine}")
                
                for i in range(len(options)): print(f"| {i+1} -> {options[i]:<43} {'|':>}")
                tools.divider()

                # Validate Options
                chosenOption = str(input('\n-> Escolha uma opção: '))

                # Show user data
                if chosenOption == '1':
                    if Account.showData() == True:
                        SenacBankSystem.init(True)
                # Deposit
                elif chosenOption == '2':
                    if Account.deposit() == True:
                        SenacBankSystem.init(True)
                
                # Withdraw
                elif chosenOption == '3':
                    if Account.withdrawCash() == True:
                        SenacBankSystem.init(True)

                # Exit System
                elif chosenOption == '4':
                    SenacBankSystem.exit()

                # Not existing function
                else:
                    os.system('cls')
                    tools.divider()
                    print(f"{'|':<} {'Digite uma opção válida!':^48} {'|':>}")
                    tools.divider()


    ## Call an Account login
    def login():
        os.system('cls')

        # Starts login loop
        while True:
            newLine =  '\n' + f"{'|':<51}" + f"{'|':>}"

            tools.divider()
            print(f"{'| Entrar em uma conta existente:':<50} {'|':>} {newLine}")
            print(f"{'| -> Numero da conta: ':<50} {'|':>}")
            tools.divider()

            # Login Informations
            accountNumber = int(input('\n-> Insira o número da conta: '))
            
            os.system('cls') # clear console
            tools.divider()
            print(f"{'| Entrar em uma conta existente:':<50} {'|':>} {newLine}")
            print(f"{'| -> Numero da conta: {}':<49} {'|':>}".format(accountNumber))
            tools.divider()

            password = str(input('\n-> Insira sua senha: '))
            
            for i in range(4):
                os.system('cls') # clear console
                tools.divider()
                print(f"{'|':<} {'Validando{}':^{50-i}} {'|':>}".format('.'*i))
                tools.divider()
                sleep(0.5)

            # Send parameters to Account class
            if Account.login(accountNumber, password) == True:
                return True       

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

# System Init
SenacBankSystem.init()
