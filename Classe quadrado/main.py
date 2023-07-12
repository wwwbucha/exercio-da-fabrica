from Quadrado import*
tamanho=float(input("TAMANHO DO LADO: "))
result=Quadrado(tamanho)
result.mostrar()
tamanho=float(input("novo lado: "))
result.alterar(tamanho)