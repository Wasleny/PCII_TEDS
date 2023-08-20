def fibonacci(tamanho_sequencia):
    array_sequencia = [0,1]

    for i in range(2, tamanho_sequencia):
      array_sequencia.append(array_sequencia[i - 1] + array_sequencia[i - 2])

    return array_sequencia

#testes
print(fibonacci(10))
print(fibonacci(5))
