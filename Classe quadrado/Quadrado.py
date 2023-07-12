class Quadrado:
    def __init__(self, tamanho):
        self.tamanho=tamanho

    def mostrar(self):
        self.area=self.tamanho*self.tamanho
        print(self.area)
        
    def alterar(self,novoValor): 
        self.tamanho=novoValor
        self.area=self.tamanho*self.tamanho
        print(self.area)