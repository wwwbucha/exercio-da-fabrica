import os
def somaimposto(a,b):
    custo=a
    imposto=b/100
    finalcusto=custo+(custo*imposto)
    return finalcusto
while True:
    try:
        a=float(input("Qual o custo do produto: "))
        b=float(input("Insira a porcentagem do imposto: "))
    except ValueError:
        os.system("cls")
        print("Digite somente numeros.")
        os.system("pause")
        os.system("cls")
    else:
        os.system("cls")
        break
valor=somaimposto(a,b)
print("O custo final será: {:.2f}R$.".format(valor))
#imprime um produto com uma taxa de imposto informada.