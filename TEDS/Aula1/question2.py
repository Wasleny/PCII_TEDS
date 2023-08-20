deposito_inicial = float(input("Digite o valor do depósito inicial: "))
taxa_juros = float(input("Digite a taxa de juros (em decimal): "))

saldo_atual = deposito_inicial
total_juros = 0.0

for mes in range(2, 25):
  saldo_atual += saldo_atual * taxa_juros
  total_juros += saldo_atual * taxa_juros
  print(f"Mês {mes} - Saldo: {saldo_atual}")

print(f"Total ganho com juros em 24 meses: {total_juros}")