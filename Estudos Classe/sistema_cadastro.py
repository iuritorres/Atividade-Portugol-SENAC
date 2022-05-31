### IMPORTAÇÕES ###

import os
from permissoes import Permissoes

### CÓDIGO ###

# TIPO DE CONTA

tipo_conta = Permissoes.conta_developer

# LISTA

lista_produtos = ['Banana', 'Cenoura', 'Abacate', 'Alface', 'Cebola']

# FUNÇÕES

def funcoes_sistema():
    print('\n','='*27,'[ CONSULTA ]','='*27,'\n')
    print(' 0 - Finalizar Consultas')
    print(' 1 - Ver os itens da lista.')
    print(' 2 - Inserir um item na lista.')
    print(' 3 - Mudar um item da lista.')
    print(' 4 - Deletar um item da lista.')
    print('\n','='*68,'\n')

def ver_itens():

    print(lista_produtos)


def inserir_item():

    item_insert = str(input(' Digite o item que desejar adicionar: '))

    confirmacao = str(input(f' Você realmente deseja inserir "{item_insert}" na lista?(SIM/NAO): ')).upper()

    if confirmacao == 'SIM':
        lista_produtos.append(item_insert)
        print(f' "{item_insert}" foi adicionado a lista.')
    elif confirmacao == 'NAO':
        print(' A solicitação foi cancelada.')
    else:
        print(' Digite SIM ou NAO.')


def mudar_item():

    item_alterado = str(input(' Digite qual item você deseja alterar na lista: '))
    
    if item_alterado in lista_produtos:
        novo_item = str(input(' Digite o item que irá substituí-lo: '))

        confirmacao = str(input(f' Você realmente deseja substituir "{item_alterado}" por "{novo_item}" na lista?(SIM/NAO): ')).upper()

        if confirmacao == 'SIM':
            posicao_item = lista_produtos.index(item_alterado)
            remover_produto = lista_produtos[posicao_item]

            lista_produtos.remove(remover_produto)
            lista_produtos.insert(posicao_item ,novo_item)

            print(f' "{item_alterado}" foi mudado por "{novo_item}" na lista.')

        elif confirmacao == 'NAO':
            print(' A solicitação foi cancelada.')

        else:
            print(' Digite SIM ou NAO.')

    else:
        print(' Esse item não existe na lista.')


def deletar_item():

    item_deletado = str(input(' Digite qual item você deseja deletar na lista: '))

    if item_deletado in lista_produtos:
        confirmacao = str(input(f' Você realmente deseja deletar "{item_deletado}" da lista?(SIM/NAO): ')).upper()

        if confirmacao == 'SIM':
            posicao_item = lista_produtos.index(item_deletado)
            remover_produto = lista_produtos[posicao_item]

            lista_produtos.remove(remover_produto)

            print(f' "{item_deletado}" foi deletado da lista.')

        elif confirmacao == 'NAO':
            print(' A solicitação foi cancelada.')

        else:
            print(' Digite SIM ou NAO.')

    else:
        print(' Esse item não existe na lista.')


# FUNCIONAMENTO

os.system('cls')

funcoes_sistema()

while True:

    id_exec_funcao_sistema = int(input(' Digite um número que corresponda a função que deseja executar: '))
    print('\n','='*68,'\n')

    if id_exec_funcao_sistema == 1:
        
        ver_itens()

    elif id_exec_funcao_sistema == 2:

        if tipo_conta == Permissoes.conta_cliente:
            print(' Você não tem acesso a essa função.')

        else:
            inserir_item()

    elif id_exec_funcao_sistema == 3:

        if tipo_conta == Permissoes.conta_funcionario:
            print(' Você não tem acesso a essa função.')

        else:
            mudar_item()

    elif id_exec_funcao_sistema == 4:

        if tipo_conta != Permissoes.conta_developer:
            print(' Você não tem acesso a essa função.')

        else:
            deletar_item()

    elif id_exec_funcao_sistema == 0:
        break

    else:
        print(' Você não digitou um número válido, tente novamente!')
