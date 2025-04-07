import random
import time

separador = "---------------------------------------------------------------"

def obter_velocidade():
  velocidade = random.randint(0, 200)
  return velocidade


def controlar_radar(velocidade):
  if velocidade > 120:
    print(f"Multe o carro: Velocidade {velocidade:.2f}Km está a cima do limite.")
    print(separador)
  else:
    print(f"Deixe o carro passar: Velocidade {velocidade:.2f}Km está dentro do limite")
    print(separador)

def monitorar():
  while True:
    velocidade = obter_velocidade()
    controlar_radar(velocidade)
    time.sleep(5)

monitorar()