cont=0
cont2=0
cont3=0
total=0
eleitores=int(input("Quantos eleitores iram votar: "))
for a in range(eleitores):
    vt = int(input("Candidato 1 \n Candidato 2 \n Candidato 3 \n"))
    if   vt == 1:
        cont+=1
    elif vt== 2:
        cont2+=1
    elif vt==3:
        cont3+=1
    total=total+1
print("O candidato João ganhou mais um voto!%d"%(cont))
print("O candidato Caio ganhou mais um voto!%d"%(cont2))
print("O candidato Junior ganhou mais um voto!%d"%(cont3))
print(total)
