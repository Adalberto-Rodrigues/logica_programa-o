"""Escreva um programa que calcule o fatorial de um número inteiro informado pelo usuário."""

# Questao 2
numero = int(input("Digite um número inteiro: "))

fatorial = 1
for i in range(1, numero + 1):
    fatorial *= i
print(f"\nO fatorial de {numero} é {fatorial}")

print("-" * 20)

