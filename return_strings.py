def inverte(nome,sobrenome):
    nomeinverso=sobrenome+','+nome
    return nomeinverso
nome=input("NOME: ")
sobrenome=input("sobrenome: ")
invertido=inverte(nome,sobrenome)
print("ola", invertido)
inverte(nome,sobrenome)