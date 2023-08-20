from typing import List

def entendendo_para_cada(vetorElementos:List, elemento_busca) -> int:
    quantidade_elementos = 0

    for elemento in vetorElementos:
        if elemento_busca == elemento:
          quantidade_elementos += 1

    return quantidade_elementos

#testes
vetor = [1,2,3,4,1,5,6,1]

print(f"quantidade: {entendendo_para_cada(vetor, 1)}")

print(f"quantidade: {entendendo_para_cada(vetor, 10)}")

print(f"quantidade: {entendendo_para_cada(vetor, 5)}")