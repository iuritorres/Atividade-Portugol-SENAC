# BIBLIOTECAS

import datetime
from time import sleep
import os

# MÓDULOS

from produtos import lista_produtos, lista_produtos, lista_produtos

# LISTAS

lista_carrinho = []
lista_valortotal_carrinho = []

# FUNÇÕES

class FuncoesPython():
    
    def __init__(self):
        pass
    
    # DATA CONCATENADA
    def data_concatenada():
        data_atual = datetime.date.today()

        dia = f'{data_atual.day:0>2}'
        mes = f'{data_atual.month:0>2}'
        ano = f'{data_atual.year:<4}'
        
        return f'{dia}/{mes}/{ano}'
    
    
    # TIMER PERSONALIZAVÉL
    def timer(tempo):

        for i in range(tempo, 0, -1):
            print('\n','='*50,'\n')
            print(' Timer acabando em {} segundos'.format(i))
            print('\n','='*50,'\n')
            sleep(1)
            os.system('cls')
            
            
    # PRINT DE PRODUTOS
    def estoque():
        print('\n====================[NOSSOS PRODUTOS]====================\n')       # Imprime os dados pessoais

        for posicao in range(0, len(lista_produtos())):
            if posicao % 2 == 0:
                print(f'{lista_produtos()[posicao]:.<30}', end='')

            else:
                print(f'R${lista_produtos()[posicao]:>6.2f}')
                
    # FUNÇÕES DAS LISTAS DO CARRINHO
    def adiciona_lista_carrinho(item):
        lista_carrinho.append(item)
    
    def mostra_lista_carrinho():
        return lista_carrinho
    
    def conta_itens_carrinho():
        resultado = len(lista_carrinho)
        return resultado

    def adiciona_lista_valortotal_carrinho(item):
        lista_valortotal_carrinho.append(item)

    def lista_valortotal_carrinho():
        return lista_carrinho
    
    def mostra_lista_produto():
        return lista_produtos
                

    # CARRINHO FINALIZADO
    def carrinho_finalizado():
        print('============ PRODUTOS NO CARRINHO: =============\n')

        for produto in FuncoesPython.mostra_lista_carrinho():
            print(f'{produto:.<30}', end='')

            preco_carrinho = (lista_produtos().index(produto) + 1)                # Acha o preço do produto na tufla
            print('R${:>6.2f}' .format(float(lista_produtos()[preco_carrinho])))                  # Imprime o preço no carrinho
            FuncoesPython.adiciona_lista_valortotal_carrinho(lista_produtos()[preco_carrinho])    # Adiciona o preço na lista do carrinho

        print('\n================= INFORMAÇÕES: =================\n')

        print('Número do pedido: #001')
        print(f'Data do pedido: {FuncoesPython.data_concatenada()}', '\n')    # Mostra a data

        valor_total_carrinho = sum(lista_valortotal_carrinho)             # Soma os preços do carrinho

        print('Quantidade de Itens: {}' .format(FuncoesPython.conta_itens_carrinho()))    # Conta quantos itens tem no carrinho
        print(f'Valor Total: R${valor_total_carrinho:6.2f}')

        print('\n================================================\n')