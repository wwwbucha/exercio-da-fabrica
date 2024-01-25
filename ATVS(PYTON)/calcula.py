print("---------------------------------------------------------------------")
print("|                      SEJA BEM VINDO A CALCULADORA                  |")
print("---------------------------------------------------------------------")

num=(input("Digite a opção > Multiplicaçao(1), Adição (2), Subtração(3) , Divisão(4) !\n" ))
if num=="1":
    a=float(input("digite o primeiro numero:"))
    b=float(input("digite o segundo numero:"))
    result=a*b
    print("o resultado e: %.2f"% (result))
elif num=="2":
    a=float(input("digite um numero:"))
    b=float(input("digite outro numero:"))
    result=a+b
    print("o resultado e: %.2f"%(result))
elif num=="3":
    a=float(input("digite o primeiro numero:"))
    b=float(input("digite o segundo numero:"))
    result=a-b
    print("o resultado e:%.2f"%(result))
elif num=="4":
    a=float(input("digite um numero:"))
    b=float(input("digite outro numero"))
    result=a/b
    print("o resultado e: %.2f"%(result))
elif num=="5":
    a=float(input("digite um numero:"))
    b=float(input("digite outro numero:"))
    result=a**b
    print("o resultado e: %.2f"%(result))
elif num=="6":
    a=float(input("digite um numero:"))
    b=float(input("digite outro numero:"))
    result=(a/b)
    print("o resultado e: %.2f"%(result))
elif num=="7":
    print("deseja sair da calculadora?")
    
print("==============================================")
    
print("-----------------------------------------")
print("|           RAIZ QUADRADA               |")
print("|                                       |")
print("-----------------------------------------")


p1=float(input("Digite o numero: "))
resul=p1**0.5
print("seu resultado é %.0f"%resul)

print("==============================================")

print("-----------------------------------------")
print("|            Area Quadrado              |")
print("|                                       |")
print("-----------------------------------------")

r1=float(input("Digite o numero para o calculo: "))
resul1=r1**2
print("sua area é: %.0f"% resul1)


print("================================================")

print("-----------------------------------------")
print("|          VOLUME DO CUBO               |")
print("|                                       |")
print("-----------------------------------------")


V1=float(input("Digite a largura: "))
v2= float(input("Digite o comprimento:  "))
v3=float(input("Digite a altura: "))


resul2=V1*v2*v3

print("seu volume do cubo é: %.0f"% resul2)

print("==================================================")

print("-----------------------------------------")
print("|       Media de 4 numeros              |")
print("|                                       |")
print("-----------------------------------------")


t1= float(input("Digite o numero: "))
t2= float(input("Digite o segundo numero: "))
t3= float(input("Digite o terceiro numero: "))
t4= float(input("Digite o quarto numero: "))

resultado=(t1+t2+t3+t4)/4

print("Sua Media é: %.0f"%resultado)

print("==================================================")

print("-----------------------------------------")
print("|            EXPONENCIAÇÃO              |")
print("|                                       |")
print("-----------------------------------------")

z1 = float(input("Digite o numero: "))
z2 = float(input("Digite o dominador: "))

resultadoz=z1**z2

print("SUA EXPO É: %.0F"%resultadoz)

print("===================================================")


print("-----------------------------------------")
print("|                FATORIAL               |")
print("|                                       |")
print("-----------------------------------------")



print("fatorial")

if a == 9:
    print("Bem vindo ao Fatorial")
    num1 = float(input("Digite um número: "))
    result=1
    contador=1
    while contador <= num1:
        result *= contador
        contador += 1
    print("O resultado é %.0f"%result)