cont=0
cont1=0
for i in range(10):
    num=int(input("Digite o numero: "))
    if num%2==0:
        cont+=1
    else:
        cont1+=1
print(cont ,"seu numero é par")
print(cont1,"seu numero é impar")