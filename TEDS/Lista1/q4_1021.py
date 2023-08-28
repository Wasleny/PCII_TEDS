valor = float(input())

print("NOTAS:")
print(f"{(valor // 100):.0f} nota(s) de R$ 100.00")
valor %= 100
print(f"{(valor // 50):.0f} nota(s) de R$ 50.00")
valor %= 50
print(f"{(valor // 20):.0f} nota(s) de R$ 20.00")
valor %= 20
print(f"{(valor // 10):.0f} nota(s) de R$ 10.00")
valor %= 10
print(f"{(valor // 5):.0f} nota(s) de R$ 5.00")
valor %= 5
print(f"{(valor // 2):.0f} nota(s) de R$ 2.00")
valor %= 2

print("MOEDAS:")
print(f"{(valor // 1):.0f} moeda(s) de R$ 1.00")
valor %= 1
print(f"{(valor // 0.5):.0f} moeda(s) de R$ 0.50")
valor %= 0.5
print(f"{(valor // 0.25):.0f} moeda(s) de R$ 0.25")
valor %= 0.25
print(f"{(valor // 0.10):.0f} moeda(s) de R$ 0.10")
valor %= 0.1
print(f"{(valor // 0.05):.0f} moeda(s) de R$ 0.05")
valor %= 0.05
print(f"{(valor / 0.01):.0f} moeda(s) de R$ 0.01")
