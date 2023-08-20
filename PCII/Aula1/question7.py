def velocidade_bola(tempo, gravidade, velocidadeInicial):
  return velocidadeInicial - gravidade * tempo

print(velocidade_bola(1, 9.81, 50))