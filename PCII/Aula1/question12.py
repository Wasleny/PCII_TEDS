def obtem_posicao_elemento(vetor, elemento):
  return vetor.index(elemento)

#teste
cores = ["azul", "roxo", "verde", "rosa", "azul"]

posicao1 = obtem_posicao_elemento(cores, "azul") #deve retornar 0
posicao2 = obtem_posicao_elemento(cores, "rosa") #deve retornar 3

print(posicao1)
print(posicao2)