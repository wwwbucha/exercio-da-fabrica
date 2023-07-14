class Pessoa:
    def __init__(self,nome,idade,endereço,cidade,estado):
        self.nome=nome
        self.idade=idade
        self.endereço=endereço
        self.cidade=cidade
        self.estado=estado

    def relatorio(self):
        print("Nome: ",self.nome)
        print("Idade: ",self.idade)
        print("Endereço: ", self.endereço)
        print("Cidade: ",self.cidade)
        print("Estado: ",self.estado)
            
    