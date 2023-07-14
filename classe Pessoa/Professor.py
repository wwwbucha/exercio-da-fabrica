class Professor(Pessoa):
    def __init__(self,salario,nome,idade,endereço,cidade,estado):
        super().__init__(nome,idade,endereço,cidade,estado)
        self.selario=salario
        print("==================================")
        print("SEJA BEM VINDO QUERIDO PROFESSOR ")
        super().relatorio()
        print("Salario.....",self.selario)
        print
        ("==================================")