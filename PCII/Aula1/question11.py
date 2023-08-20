def somatorio(n):
  soma = 0
  for i in range(2, n + 2, 2):
    soma += 1 / i

  return soma

#testes
print(somatorio(1))
print(somatorio(10))
print(somatorio(100))

