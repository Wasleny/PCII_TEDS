n = int(input("Digite o valor de 'n' para gerar os primeiros 'n' números da série de Fibonacci: "))
print(f"Os primeiros {n} números da série de Fibonacci são: ");

a = 0
b = 1

for i in range(0, n):
  if i <= 1:
    fib = i;
  else:
    fib = a + b
    a, b = b, fib

  print(f"{fib} ")