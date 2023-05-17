mininota=0
max=10
a = float(input("Digite a primeira nota: "))
b = float(input("Digite a segunda nota: "))
media=(a+b)/2
if media>=7 and media<=10:
    print("Aprovado")
    if media==10:
        print( " Distinaçao.")
elif media<7 and media>= 0:
    print("Reprovado")
else:
    print("Media invalida")