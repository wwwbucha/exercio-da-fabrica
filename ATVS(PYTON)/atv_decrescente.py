a = float(input("Digite o primeiro numero: "))
b = float(input("Digite o segundo numero:  "))
c = float(input("Digite o terceiro numero: "))

if a==b and b==c and c==b: 
    print("Todos os numeros são iguais!")
elif a==b or b==c or c==b: 
    print("Erro. Existe dois numeros iguais.")
else: 
    list=[a,b,c]
    list.sort(reverse=True)
    print("A ordem decrescente é:  {}".format(list))