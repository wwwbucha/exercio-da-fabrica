import os

def conversordehoras(hora,minutos):
    if hora<= 12 and hora>=0:
        print(hora,":", minutos ,"AM")
    elif hora> 12 and hora<=23:
        print(hora-12,":",minutos,"PM")
    else:
        print("VALOR INVALIDO")


while True:
    try:
        hora = int(input("INFORME A HORA: "))
        minutos = int(input("INFORME OS MINUTOS:? "))
    except:
        print("VALOR INVALIDO")
    else:
        if minutos>59:
            print("VALOR INVALIDO")
            continue
        conversordehoras(hora,minutos)