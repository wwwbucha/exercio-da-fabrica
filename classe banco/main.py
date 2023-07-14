from Banco import*

cont=conta("Christian",1700,12345,"chris")
cont.extrato("chris")
cont.depositar(200)
cont.sacar(400,"chrisf")
print (cont.nome)
# print (cont.__saldo)