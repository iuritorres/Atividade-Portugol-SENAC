# IMPORTAÇÕES

from ast import While
import os
from time import sleep

# LISTAS

lista_produtos = ['Maçã', 'Banana', 'Melancia', 'Abóbora', 'Batata', 'Cebola', 'Alface', 'Tomate']
preço = [2, 1, 8, 10, 3, 1.50, 0.75, 0.60]
lista_carrinho = []

# CARDÁPIO - IMPRESSAO

print('\n===============[NOSSOS PRODUTOS]===============\n')       # Imprime os dados pessoais

print('Maçã = R$2,00\n')
print('Banana = R$1,00\n')
print('Melancia = R$8,00\n')
print('Abóbora = R$10,00\n')
print('Batata = R$3,00\n')
print('Cebola = R$1,50\n')
print('Tomate = R$0,75\n')
print('Alface = R$0,60\n')

print('\n===============================================\n')       # DIVISÓRIA

### SISTEMA CARRINHO

# SISTEMA DE ADIÇÃO DE PRODUTOS

for produto_cadastrado in lista_produtos:                          # Apenas cria uma variavel para os itens da lista_produtos
    print(' ')

while True:

    produto = input('Insira um produto: ')                         # Armazena uma informação

    if produto == '0':                                             # Se digitar 0 fecha o carrinho

        break

    elif produto == produto_cadastrado in lista_produtos:
        lista_carrinho.append(produto)
        print('\n Carrinho: {}'.format(lista_carrinho))
        print('\n {} foi adicionado ao carrinho, escolha outro produto ou digite "0" para fechar o carrinho. \n'.format(produto))

    else:
        print('Ei!, não temos esse produto em nossa loja, verifique nossos produtos na tabela a cima!\n')

os.system('cls')


# TIMER PARA FINALIZAÇÃO DO PEDIDO

timer_fechamento_carrinho = [3, 2, 1]

for segundo_timer_carrinho in timer_fechamento_carrinho:
    print('\n===============================================\n', '\nCarrinho Fechado!! \n', '\nPróxima etapa em {} segundos\n' .format(segundo_timer_carrinho), '\n===============================================\n')       # DIVISÓRIA

    sleep(1)
    os.system('cls')

sleep(0.5)                                                         # Espera meio segundo para limpar a tela
os.system('cls')                                                   # Limpa a tela

print('======= PRODUTOS NO CARRINHO: =======\n')

for produto in lista_carrinho:
    print('- {}' .format(produto))

print('\n============ INFORMAÇÕES: ============\n')

print('Quantidade de Itens: {}' .format(len(lista_carrinho)) )
print('Valor Total: {}\n')