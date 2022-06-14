### DESENVOLVEDOR : IURI TORRES ###

# BIBLIOTECAS

import os
from time import sleep

# MÓDULOS

from produtos import lista_produtos
from funcoes import FuncoesPython

# PRODUTOS DA LOJA - IMPRESSAO

FuncoesPython.estoque()

### SISTEMA CARRINHO ###

# SISTEMA DE ADIÇÃO DE PRODUTOS

while True:

    print('\n=========================================================\n')   # DIVISÓRIA

    produto = input('Insira um produto: ')                         # Armazena uma informação

    if produto == '0':                                             # Se digitar 0 fecha o carrinho

        break

    elif produto in lista_produtos():
        FuncoesPython.adiciona_lista_carrinho(produto)

        os.system('cls')

        FuncoesPython.estoque()

        print('\n=========================================================\n')       # DIVISÓRIA

        print('\nCarrinho: {}\n'.format(FuncoesPython.mostra_lista_carrinho()))
        print('\n{} foi adicionado ao carrinho!\nEscolha outro produto ou digite "0" para fechar o carrinho. \n'.format(produto))

    else:

        os.system('cls')

        FuncoesPython.estoque()

        print('\nCarrinho: {}\n'.format(FuncoesPython.mostra_lista_carrinho()))
        print('Ei!, não temos {} em nossa loja, verifique nossos produtos na tabela a cima!\n' .format(produto))

os.system('cls')


# TIMER PARA FINALIZAÇÃO DO PEDIDO

FuncoesPython.timer(3)
os.system('cls')

# INFORMAÇÕES - CARRINHO FECHADO

FuncoesPython.carrinho_finalizado()