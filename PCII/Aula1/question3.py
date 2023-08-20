valor = int(input('Informe um número: '))

fatorial = 1;

for i in range(1, valor+1):
  fatorial *= i

print(f"O fatorial do número {valor} é {fatorial}")