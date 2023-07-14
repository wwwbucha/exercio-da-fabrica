from pessoa import *
class Aluno(Pessoa):
    def __init__(self,mensalidade,nome,idade,endereço,cidade,estado):
        super().__(nome,idade,endereço,cidade,estado)
        self.mensalidade=mensalidade
        print("==========================")
        print("SEJA BEM VINDO QUERIDO ALUNO")
        super().relatorio()
        print("mensalidade: ", self,mensalidade)
        print("==========================")