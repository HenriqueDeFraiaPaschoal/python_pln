import Levenshtein
import argparse
parser = argparse.ArgumentParser(description='Exemplo de script que usa dois argumentos de linha de comando do mesmo tipo.')

# Adiciona argumentos
parser.add_argument('mensagem1', type=str, help='A primeira mensagem a ser impressa.')
parser.add_argument('mensagem2', type=str, help='A segunda mensagem a ser impressa.')

# Analisa os argumentos
args = parser.parse_args()

# Usa os argumentos
print("Mensagem 1:", args.mensagem1)
print("Mensagem 2:", args.mensagem2)

def carregar_perguntas(arquivo):
  perguntas_respostas = {}
  with open(arquivo, "r") as f:
    for linha in f:
      pergunta, resposta = linha.strip().split("|")
      perguntas_respostas[pergunta.lower()] = resposta


  return perguntas_respostas

def encontrar_resposta(pergunta, perguntas_respostas, limiar_distancia=5):
  menor_distancia = float("inf")
  melhor_resposta = ""
  for p, r in perguntas_respostas.items():
    distancia = Levenshtein.distance(pergunta, p)
    if distancia < menor_distancia:
      menor_distancia = distancia
      melhor_resposta = r
  if menor_distancia <= limiar_distancia:
      return melhor_resposta
  else:
      return "Pergunta não encontrada."

if __name__ == "__main__":
  perguntas_respostas = carregar_perguntas("perguntas.txt")
  limiar_distancia = 20
  pergunta = "quem criou você?"
  resposta = encontrar_resposta(pergunta, perguntas_respostas, limiar_distancia)
  print("Resposta:", resposta)
