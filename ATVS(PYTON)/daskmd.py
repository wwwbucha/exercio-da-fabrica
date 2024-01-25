class Vendedor():
    def __init__(self,nome,vendas):
        self.nome=nome
        self.vendas=vendas
    def vendeu(self,vendas):
        self.vendas=vendas
        self.vendas
        print(self.vendas)
    def bateu_meta(self,meta):
        if self.vendas>meta:
            print("bateu a meta.")
        else:
            print("não bateu a meta.")
vendedor1=Vendedor("ederson",100)
print(vendedor1.nome)
vendedor1.bateu_meta(100)














vendedor1=Vendedor('Ederson',1000)
print(vendedor1.vendas,"\n",vendedor1.nome)
