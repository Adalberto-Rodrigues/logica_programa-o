#exercicio_06
"""Jogo de Adivinhação Crie um jogo onde o programa escolhe um número aleatório entre 1 e 100.
O jogador deve tentar adivinhar o número. Obs. Pesquisa como importar e usar o módulo random para
gerar o número aleatório em questão."""

#A cada tentativa, o programa deve dizer se o número é maior ou menor que a tentativa.
#O jogo termina quando o jogador adivinhar o número correto.

print("Resposta")
import random
numero_secreto = random.randint(1, 100)

print("🎯 Jogo de Adivinhação 🎯")
print("Tente adivinhar o número entre 1 e 100.")

tentativas = 0

while True:
    # Lê a tentativa do jogador
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite < numero_secreto:
        print("📉 O número é MAIOR que isso!")
    elif palpite > numero_secreto:
        print("📈 O número é MENOR que isso!")
    else:
        print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
        break
