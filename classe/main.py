from Conta import *
import os
print('--- Bem vindo ao Banco ---')
while True:
    try:
        menu = input('O que deseja fazer:\n[1] - Realizar cadastro\n[2] - Sacar dinheiro\n[3] - Depositar dinheiro\n[4] - Extrato da conta\n[0] - Voltar\n>')
        os.system("cls")

        if menu == '1':
            print('--- Cadastro ---')
            nome = input('Digite seu nome: ')
            conta = input('Informe sua conta aqui: ')
            agencia = int(input('Informe o número da agencia aqui: '))
            fone = input('Informe seu número de telefone aqui: ')
            cpf = int(input('Informe seu CPF: '))
            saldo = float(input('Informe seu saldo: R$'))
            conta1 = Conta(nome,conta,agencia,fone,cpf,saldo)
            os.system("cls")


        elif menu == '2':
            print('--- Saque ---')
            sacarDinheiro = float(input('Quantos deseja sacar?: R$'))
            conta1.sacar(sacarDinheiro)
            print(conta1.sacar)
            os.system("cls")
            if sacarDinheiro > saldo:
                print('Você não possui esse valor na conta')
                os.system("pause")
                os.system("cls")


        elif menu == '3':
            print('--- Deposito ---')
            depositoDeDinheiro = float(input('Quantos deseja depositar?: R$'))
            conta1.deposito(depositoDeDinheiro)
            print(conta1.deposito)
            os.system("cls")


        elif menu == '4':
            print('--- Extrato ---')
            conta1.extrato()
            os.system("pause")
            os.system("cls")


        elif menu == '0':
            break


        else: 
            print('Opção inválida')
            os.system("pause")
            os.system("cls")

    except ValueError:
       print('X| Digite apenas números |X')
    except:
        print('X| Erro desconhecido |X')