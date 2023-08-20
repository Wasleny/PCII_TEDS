def altura_bola(tempo, gravidade, velocidadeInicial):
    return velocidadeInicial * tempo - (gravidade * tempo ** 2) / 2

def velocidade_bola(tempo, gravidade, velocidadeInicial):
  return velocidadeInicial - gravidade * tempo

def velocidade_altura_bola(velocidade_inicial, gravidade, n):
    for tempo in range(1, n):
      print(f"Altura: {altura_bola(tempo, gravidade, velocidade_inicial)}")
      print(f"Velocidade: {velocidade_bola(tempo, gravidade, velocidade_inicial)}")

#teste
velocidade_altura_bola(50, 9.81, 20)