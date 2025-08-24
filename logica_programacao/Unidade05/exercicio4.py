#exercicio_04
"""Escreva um programa que leia uma sequência de números inteiros informados pelo usuário e imprima os números ímpares dessa sequência."""
print("Resposta")
entrada = input("Digite números inteiros separados por espaço: ")

# Converte a entrada para uma lista de inteiros
numeros = list(map(int, entrada.split()))

# Filtra apenas os ímpares
impares = [n for n in numeros if n % 2 != 0]

# Exibe os números ímpares
print("\nNúmeros ímpares na sequência:")
if impares:
    print(*impares)
else:
    print("Nenhum número ímpar encontrado.")