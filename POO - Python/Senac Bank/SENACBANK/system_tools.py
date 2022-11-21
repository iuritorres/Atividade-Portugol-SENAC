import os
from time import sleep

class Tools:
    # Divider
    def divider():
        print('+'+'-'*50+'+')

    # Message Printer
    def showMessage (*mensagem):
        os.system('cls')
        print('+'+'-'*50+'+')
        for msg in mensagem:
            print(f"|{msg:^50}|")
        print('+'+'-'*50+'+')

    def validateTimer(operacao):
        for i in range(4):
            os.system('cls') # clear console

            mensagem = operacao
            mensagem += ('.' * i)

            Tools.divider()
            print(f"|{mensagem:^50}|")
            Tools.divider()

            sleep(0.5)