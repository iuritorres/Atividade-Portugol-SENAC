# Users DataBase
validUsers = [
    {
        'accountNumber': 791,
        'owner': 'João Vitor Souza da Silva',
        'balance': 1300.54,
        'password': 'joao123'
    },
    {
        'accountNumber': 575,
        'owner': 'Iuri Barbosa Torres',
        'balance': 3870.90,
        'password': 'iuri123'
    },
    {
        'accountNumber': 367,
        'owner': 'Ketlen Joyce Muniz Silva Lopes',
        'balance': 7834.98,
        'password': 'joyce123'
    }
]

class BancoDeDados:

    def getUser():
        return validUsers
    
    def setUser(User):
        validUsers.append(User)
