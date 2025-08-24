#exercicio_01
"""Escreva uma função que receba uma lista de números e retorne o valor mínimo encontrado."""
print("Resposta")

def encontrar_minimo(lista):
    if not lista:  # verifica se a lista está vazia
        return None
    minimo = lista[0]  # assume o primeiro como menor
    for numero in lista:
        if numero < minimo:
            minimo = numero
    return minimo


# Exemplo de uso:
entrada = input("digite numeros separados por virgulas e espaço")

#converte a string em lista inteiros
lista_numeros =[int(x.strip()) for x in entrada.split(",")]

print("O valor mínimo é:", encontrar_minimo(lista_numeros))
