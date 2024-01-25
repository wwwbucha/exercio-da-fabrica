'''def hello (nome,idade):
    print("Ola", nome,"\nSua idade é: ", idade)
hello("ederson",25)'''


def calculador_pagamentos(qtd_horas,valor_hora): 
    horas=float(qtd_horas)
    taxa=float(valor_hora)
    if horas <= 48:
        salario=horas*taxa
    else:
        h_excd=horas-40
        salario=40*taxa+(h_excd*(1.5*taxa))
        print(salario)
a=float(input("DIGITE A SUA HORA: "))
b=float(input("Digite o valor da sua hora: "))
calculador_pagamentos(a,b)


