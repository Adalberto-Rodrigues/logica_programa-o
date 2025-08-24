#exercicio_03
"""Escreva um programa que leia uma sequência de números inteiros
 informados pelo usuário e imprima os números primos dessa sequência."""

print("Resposta")
# Função para verificar se um número é primo
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

entrada = input("Digite números inteiros separados por espaço: ")
# Converte a entrada para uma lista de inteiros
numeros = list(map(int, entrada.split()))

# Filtra apenas os números primos
primos = [n for n in numeros if eh_primo(n)]
print("-" * 20)

# Exibe os números primos
print("\nNúmeros primos na sequência:")
if primos:
    print(*primos)
else:
    print("Nenhum número primo encontrado.")
    print("-" * 30 )
