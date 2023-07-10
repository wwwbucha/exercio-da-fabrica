class Conta():
    def __init__(self,nome,conta,agencia,fone,cpf,saldo=0):
        self.nome = nome
        self.conta = conta
        self.agencia = agencia
        self.fone = fone
        self.cpf = cpf
        self.saldo = saldo
    

    def extrato(self):
        print('R$',self.saldo)


    def sacar(self,saque):
        if self.saldo <= saque:
            self.saldo = self.saldo - saque


    def deposito(self,deposit):
        self.saldo =self.saldo + deposit