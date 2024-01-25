number=[]
while True:
    num=input("DIGITE O NUMERO: ")
    if num=="x":
        break
    num=int(num)
    number.append(num)
print("O maior número é:",max(number),"\nO menor número é:",min(number),"\nA soma de todos é:",sum(number)) #Printa os resultados.
    