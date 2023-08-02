from Ford import*
from Carro import*
from Orcamento import*
from CompraVeiculo import*
print("+++++++++++++++++++++++++++++++")
print("|        SEJA BEM VINDE       |")
print("|            A FORD           |")
print("+++++++++++++++++++++++++++++++")

print ("Olá , QUAL FUNCIONALIDADE VC GOSTARIA: ")
print("1- CADASTRO FUNCIONARIO")
print("2- REVISÃO ")
print("3- ORCAMENTO")
print("4- COMPRA DE VEICULO")
print("0- SAIR")


opc=input("ESCOLHA SUA OPC: ")
if opc == '1':

    nome = input('Digite o nome: ')
    sobrenome = input('Digite o sobrenome: ')
    telefone = input('Digite o Telefone: ')
    cpf = input('Digite o cpf: ')
    funcionario1 = Funcionario(nome,sobrenome,telefone,cpf)

if opc == '2':
    nmdodono=input("NOME DO DONO: ")
    celular=input("TELEFONE: ")
    mdcarro=input("MODELO CARRO: ")
    carro1 = Carro(nome,telefone,mdcarro)

if opc == '3':
    nomepeca=(input("Digite o nome da peca: "))
    valorpeca=float(input("Digite o valor da peca: "))
    quantidade=float(input("DIGITE A QUANTIDADE : "))
    x = Orcamento(nomepeca, valorpeca, quantidade)
    x.orcamentoValor(valorpeca, quantidade)
if opc == '4':
    nome1==input("Digite seu nome: ")
    rg=input("Digite seu rg: ")
    cpf=input("Digite seu cpf: ")
    endereço=input("Digite seu endereço: ")
    Comprasveiculo = CompraVeiculo(nome,rg,cpf,endereço)    