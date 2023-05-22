

print("=================================================================")
print("|              seja bem vindo a lista de                        |")
print("|                      cadastro                                 |")
print("=================================================================")


nomm=[]
sobrenomm=[]
enderecoo=[]
bairroo=[]
cidadee=[]
estadoo=[]
paiss=[]
fonee=[]
cpff=[]
pesoo=[]
alturaa=[]
idadee=[]
ncartaoo=[]
emaill=[]
cepp=[]
nota11=[]
nota22=[]
nota33=[]
nota44=[]
mediaa=[]
seriee=[]
classee=[]
sexoo=[]
corr=[]
registroo=[]
while True:
        
        
    nome=(input("Digite seu nome: "))
    print(nome.capitalize())
    sobrenome = (input("Digite seu sobrenome: "))
    print(sobrenome.capitalize())
    endereco=(input("Digite seu endereço: "))
    print(endereco.capitalize())
    bairro=(input("Digite seu bairro: "))
    print(bairro.capitalize())
    cidade=(input("Digite a cidade: "))
    print(cidade.capitalize())
    estado=(input("Digite seu estado: "))
    print(estado.capitalize())
    pais=(input("Digite seu pais: "))
    print(pais.capitalize())
    fone=(input("Digite seu numero de telefone: "))
    cpf=str(input("Digite seu CPF: "))
    Peso=float(input("Digite seu peso: "))
    altura=float(input("Digite sua altura: "))
    idade=(input("Digite sua idade: "))
    ncartao=float(input("Digite seu numero do cartão: "))
    email=input("Digite seu email: ")
    cep=int(input("Digite seu cep: "))
    nota1=float(input("Digite a sua primeira nota: "))
    nota2=float(input("Digite a sua segunda nota: "))
    nota3=float(input("Digite a sua terceira nota: "))
    nota4=float(input("Digite a sua quarta nota: "))
    media=(nota1+nota2+nota3+nota4)/4
    print("Sua media é: ",media)
    serie=input("Digite sua serie: ")
    classe=str(input("Digite sua classe: "))
    print(classe.capitalize())
    sexo=input("Digite seu sexo: ")
    cor=input("Digite a sua cor de pele: ")
    pare=input("voce deseja continuar S/N: ")
    if pare=="N":
        break

    nomm.append(nome)
    sobrenomm.append(sobrenome)
    enderecoo.append(endereco)
    bairroo.append(bairro)
    cidadee.append(cidade)
    estadoo.append(estado)
    paiss.append(pais)
    fonee.append(fone)
    cpff.append(cpf)
    pesoo.append(Peso)
    alturaa.append(altura)
    idadee.append(idade)
    ncartaoo.append(ncartao)
    emaill.append(email)
    cepp.append(cep)
    nota11.append(nota1)
    nota22.append(nota2)
    nota33.append(nota3)
    nota44.append(nota4)
    mediaa.append(media)
    seriee.append(serie)
    classee.append(classe)
    sexoo.append(sexo)
    corr.append(cor)
print(nome)
print(sobrenome)
print(endereco)
print(bairro)
print(cidade)
print(estado)
print(pais)
print(fone)
print(cpf)
print(Peso)
print(altura)
print(idade)
print(ncartao)
print(email)
print(cep)
print(nota1)
print(nota2)
print(nota3)
print(nota4)
print(media)
print(serie)
print(classe)
print(sexo)
print(cor)