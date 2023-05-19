print("|----------SEJA BEM VINDO----------|")#a parte de seja bem vindo 
a = input("   Digite o numero ou Palavra: ")#aqui é pra pessoa digitar o numeor ou palavra
if str(a) == "".join(reversed(a)) :#a variavel vai ver se vai funcionar
    print("   É um Palindrome")#aqui mostra se é palindrme 
else:
    print("   Não é Palindrome")#aqui se não for palindrome