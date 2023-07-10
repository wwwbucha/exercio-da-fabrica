from bola import*
import os
escolha=1
while escolha != 0:
    try:
        print("0-sair")
        print("1-para a bola rolar")
        print("2-para ela pingar")
        print("3-para ver a circunferencia da bola")
        print("4-para ver a cor da bola")
        print("5-para ver o tecido da bola")
        escolha=int(input("digite: "))
        escolha2= bola(escolha)
    except:
        print("valor invalido...")
    os.system("pause")
    os.system("cls")