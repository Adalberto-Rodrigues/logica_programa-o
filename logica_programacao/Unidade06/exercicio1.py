# Exercicio_01
"""Crie um programa que solicite ao usuário que insira 10 palavras. Armazene essas palavras em uma lista. Depois:"""
#a) Exiba a lista na ordem inversa.
#b) Substitua todas as palavras que começam com a letra "a" por ***. 
#c) Exiba a lista modificada.

print("Resposta")
palavras = []

for i in range(10):
    palavra = input(f"Digite a {i+1}ª palavra: ")
    palavras.append(palavra)

# Exibir a lista na ordem inversa
print("\nLista na ordem inversa:")
print(list(reversed(palavras)))  # ou palavras[::-1]

# Substituir palavras que começam com 'a' ou 'A' por ***
for i in range(len(palavras)):
    if palavras[i].lower().startswith("a"):
        palavras[i] = "*"

# Exibir a lista modificada
print("\nLista modificada:")
print(palavras)