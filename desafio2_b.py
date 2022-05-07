# IMPORTAÇÕES


# CÓDIGO

nome1 = input('Qual o seu nome? ')                                # Armazena nome1
idade1 = int(input('Qual a sua idade? '))                         # Armazena idade1
sexo1 = input('Qual o seu sexo? (M/F): ')                         # Armazena sexo1

nome2 = input('Qual o seu nome? ')                                # Armazena nome2
idade2 = int(input('Qual a sua idade? '))                         # Armazena idade2
sexo2 = input('Qual o seu sexo? (M/F): ')                         # Armazena sexo2

# CONDIÇÃO DE EXIBIÇÃO DE NOME (SEXO MASCULINO COM MAIS DE 21 ANOS)

if idade1 and idade2 > 21 and sexo1 == 'M' and sexo2 == 'M':
    print('Nome: \n\n - {} \n - {}'.format(nome1, nome2))

elif idade1 > 21 and sexo1 != 'F':
    print('Nome: \n\n - {}'.format(nome1))

elif idade2 > 21 and sexo2 != 'F':
    print('Nome: \n\n - {}'.format(nome2))