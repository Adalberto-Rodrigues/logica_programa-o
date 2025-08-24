#exercicio_02
"""Escreva uma função que receba uma lista de números 
e um valor inteiro n, e retorne uma nova lista com os n primeiros valores da lista original."""

print("Resposta")
def primeiros_n(lista, n):
    # retorna os n primeiros elementos da lista
    return lista[:n]


# Exemplo de uso:
entrada = input("digite numeros separados por virgulas e espaço")

#converte a string em lista inteiros
lista_numeros =[int(x.strip()) for x in entrada.replace(",", " ").split()]

n = int(input("digite a quantidade de elementos que deseja:"))

print (f"Os{n}primeiros numeros são: {primeiros_n(lista_numeros, n)}")
