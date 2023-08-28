import random

lista = []
i = 0
while i < 20:
  lista.append(random.randint(1, 100))
  i+=1

listaPar = []
listaImpar = []
for num in lista:
  if num % 2 == 0:
    listaPar.append(num)
  else:
    listaImpar.append(num)

print(lista)
print(listaPar)
print(listaImpar)
