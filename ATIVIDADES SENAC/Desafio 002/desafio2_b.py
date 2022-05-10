### DESENVOLVEDORES : RAFAEL LUÍS | IURI TORRES ###

# IMPORTAÇÕES

from ast import While
from operator import index
import os
from time import sleep
import datetime

from numpy import true_divide

# CÓDIGO
lista_nome = []
lista_idade = []
lista_sexo = []

nome = ''
idade = ''
sexo = ''

while True:
    print('\n','='*57,'\n')                                              # DIVISÓRIA

    print(' Digite 0 nos 3 campos para parar a consulta!\n')             # DIVISÓRIA

    if nome != '0':
                  

        nome = input(' Qual o seu nome? ').upper()                                   # Armazena nome

        lista_nome.append(nome)

        
        idade = int(input(' Qual a sua idade? '))                             # Armazena idade

        lista_idade.append(idade)

        sexo = str(input(' Qual o seu sexo? (M/F): ')).upper()                # Armazena sexo1

        if sexo[0] == 'M':                                                   # valição do sexo
            sexo = 'M'

        elif sexo[0] == 'F':
            sexo = 'F'

        lista_sexo.append(sexo)                                             # Fechamento da validção
    elif nome == '0':

        break                                                  

os.system('cls')

print('\n','='*57,'\n')   # DIVISÓRIA

# CONDIÇÃO DE EXIBIÇÃO DE NOME (SEXO MASCULINO COM MAIS DE 21 ANOS)
for nome in lista_nome:
    posicao_nome = lista_nome.index(nome)

    nome = lista_nome[posicao_nome]
    idade = lista_idade[posicao_nome]
    sexo = lista_sexo[posicao_nome] 

    if idade > 21 and sexo == 'M' :
        
        print('Nome: \n\n - {} '.format(nome))
