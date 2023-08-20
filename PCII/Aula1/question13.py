def operacao_vetor(vetor):
  if len(vetor) == 0:
    return 0
  else:
    return (min(vetor) + max(vetor)) / 2

print(operacao_vetor([4, 6, 7, 12, 9]))