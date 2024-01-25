a=input("qual periodo voce estuda?Matutino, Vespertino, Noturno? (M/V/N)\n")
a=a.capitalize()


if a=="M":
    print("BOM DIA")
elif a=="V":
    print("BOA TARDE")
elif a=="N": 
    print("BOA NOITE")
else: 
    print("valor invalido")
    