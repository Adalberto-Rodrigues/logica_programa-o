# Exercicio_04
"""Elabore um programa que Dada a seguinte tupla de frutas:"""

#frutas = ("banana", "maçã", "uva", "laranja", "maçã", "melancia", "uva")

#Pergunte ao usuário o nome de uma fruta. Informe quantas vezes essa fruta aparece na tupla.
#Se a fruta estiver presente, mostre o índice da primeira ocorrência. Caso contrário, exiba uma mensagem informando que a fruta não foi encontrada.

print("Resposta")

frutas = ("banana", "maçã", "uva", "laranja", "maçã", "melancia", "uva")
fruta_busca = input("Digite o nome de uma fruta: ").strip().lower()

# para que não dê problema em relação as letras maiúsculas/minúsculas
frutas_normalizadas = tuple(f.lower() for f in frutas)
quantidade = frutas_normalizadas.count(fruta_busca)

if quantidade > 0:
    indice = frutas_normalizadas.index(fruta_busca)
    print(f"A fruta '{fruta_busca}' aparece {quantidade} vez(es) na tupla.")
    print(f"Primeira ocorrência no índice: {indice}")
else:
    print(f"A fruta '{fruta_busca}' não foi encontrada na tupla.")