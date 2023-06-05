import os
while True:
    try:
        print("1- CADASTRO CLIENTE")
        print("2- CADASTRO PASSAGEM")
        print("3- CADASTRO AVIAO")
        print("4- CADASTRO TRIPULAÇAO")
        opcoes=int(input("Selecione a opção: "))
    except ValueError:
        print("O VALOR DIGITADO NAO É UM NÚMERO!")
        print("TENTE NOVAMENTE...")
        os.system("pause")
        continue
    if opcoes==1:
        while True:
            nome=input("nome: ")
            sobrenome=(input("sobrenome: "))
            fone=input("fone: ")
            idade=(input("idade: "))
            try: 
                rg=float(input("RG: "))
                cpf=float(input("cpf: "))
            except ValueError:
                print("tente novamente... o valor nao é um numero inteiro.")
                os.system("pause")
                os.system("cls")
    
    if opcoes==2:
        try:
            destino=(input("destino: "))
            origem=(input("origem: "))
            duraçao=(input("duraçao: "))
            valorpass=int(input("valor da passagem: "))
            desconto=(valorpass*00.5) - valorpass
            print(desconto)
        except ValueError:
            print("O ERRO")
    if opcoes==3:
        modelo=(input("Digite o modelo do avião: "))
        ano=(input("Digite o ano do avião: "))
        hrsvoo=(input("Digite a hr de voo: "))
        cor=("Digite a cor do avião: ")
        qntpassa=int(input("Digite a quantidade de passageiro: "))
        
    if opcoes==4:
        nome=(input("Digite o nome da tripulção: "))
        decargo=(input("Digite a descrição do cargo: "))
        dtadmissão=(input("Digite a data da admissção: "))
        fonee=int(input("Digite o seu fone: "))
    print("tenha um otimo dia!")