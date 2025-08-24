#exercicio_05
"""Escreva um programa que leia uma sequência de números inteiros informados pelo usuário e imprima a quantidade de números negativos."""

print("Resposta")
# Lê a sequência de números
entrada = input("Digite números inteiros separados por espaço: ")

# Converte para lista de inteiros
numeros = list(map(int, entrada.split()))

# Conta os números negativos
qtd_negativos = sum(1 for n in numeros if n < 0)

# Exibe o resultado
print(f"\nQuantidade de números negativos: {qtd_negativos}")