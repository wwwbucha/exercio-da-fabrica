def par(x):
    if(x%2)==0:
        return True
    else:
        return False
while True:
    num=int(input("insira o numero: "))
    if par(num):
        print("é par")
    else:
        print("é impar")
par(x)