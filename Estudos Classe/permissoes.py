class Permissoes:
    def __init__(self, tipo_conta):
        self.tipo_conta = tipo_conta

    # TIPOS DE CONTA

    def conta_cliente(self):
        self.tipo_conta = 'conta_cliente'


    def conta_funcionario(self):
        self.tipo_conta = 'conta_funcionario'


    def conta_developer(self):
        self.tipo_conta = 'conta_developer'

