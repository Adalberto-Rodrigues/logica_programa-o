#exercicio_01
"""Escreva um programa que imprima a tabuada (Multiplicação) de um número inteiro informado pelo usuário. Imprima a tabuada de maneira organizada."""

print("Resposta")
numero = int(input("Digite um número inteiro da tabuada: "))

print(f"\nTabuada do {numero}")
print("-" * 20)

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i:2} = {resultado}")

print("-" * 20)

