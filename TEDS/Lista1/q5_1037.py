valor = float(input())
intervalo = ''

if valor >= 0 and valor <= 25:
    intervalo = "[0,25]"
elif valor > 25 and valor <= 50:
    intervalo = "(25,50]"
elif valor > 50 and valor <= 75:
    intervalo = "(50,75]"
elif valor > 75 and valor <= 100:
    intervalo = "(75,100]"
else:
    intervalo = ''

if intervalo != '':
    print(f"Intervalo {intervalo}")
else:
    print("Fora de intervalo")