class retangulo:
    def __init__(self,ladoA,ladoB):
        self.ladoA=ladoA
        self.ladoB=ladoB

    def mudarvalor(self,novoA,novoB):
        self.ladoA=novoA
        self.ladoB=novoB

    def rodape(self):
        pass

    def retornar(self):
        self.area=self.ladoA*self.ladoB
        self.perimetro=self.ladoA*2+self.ladoB*2
        print(f"O VALOR DO LADO A {self.ladoA}")
        print(f"O VALOR DO LADO B {self.ladoB}")
        print(self.perimetro,self.area) 