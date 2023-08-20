import math

def delta(a,b,c):
  return (b ** 2) - (4 * a * c)

def funcaoSegundoGrau(a, b, c):
  valorDelta = delta(a, b, c)

  if valorDelta < 0:
    print("O valor de delta é menor que zero")
  else:
    x1 = (-b + math.sqrt(valorDelta)) / (a * 2)
    x2 = (-b - math.sqrt(valorDelta)) / (a * 2)
    if valorDelta == 0:
      print(f"Só existe uma raiz. Valor de x: {x1}")
    else:
      print(f"Valores de x: {x1}, {x2}")


funcaoSegundoGrau(3, 0, -27)
funcaoSegundoGrau(1, -1, -12)
funcaoSegundoGrau(5, -45, 0)
funcaoSegundoGrau(2, -8, 8)