def altura_bola(tempo, gravidade, velocidadeInicial):
    return velocidadeInicial * tempo - (gravidade * tempo ** 2) / 2

print(f"Altura 1: {altura_bola(1, 9.81, 50)}")