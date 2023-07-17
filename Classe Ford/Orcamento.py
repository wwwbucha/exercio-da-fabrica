
class Orcamento:
    def __init__(self,nomepeca,valorpeca,quantidade):
        self.nomepeca=nomepeca
        self.valorpeca=valorpeca
        self.quantidade=quantidade
    
    
    def orcamentoValor(self,valorpeca,quatidade): 
        self.valorpeca = valorpeca
        self.quantidade = quatidade
        print(self.quantidade * self.valorpeca)
        
  
