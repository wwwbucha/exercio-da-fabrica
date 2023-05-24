print("-- Resevartório de Água --")

altura=float(input(" Digite a altura (cm):"))
largura=int(input(" Digite a largura (cm): "))
comprimento=float(input(" Digite o comprimento (cm): "))
c_diário=float(input("Digite o valor do consumo médio diário(litros/dia)= "))

cap_total=((altura*largura*comprimento)/1000)
auton_reser=cap_total/c_diário

print("Capacidade do Reservatório= ",cap_total, "litros ")
print("Autonomia do reservatório= ",auton_reser," dias") 
if(auton_reser<2):
    print("Consumo Elevado")
elif(auton_reser>=2 and auton_reser<7):
    print("Consumo Moderado")
elif(auton_reser>7):
    print("\n Consumo Baixo")