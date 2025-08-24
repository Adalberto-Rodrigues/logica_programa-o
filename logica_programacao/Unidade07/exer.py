def encontrar_minimo(lista):
    if not lista:  # verifica se a lista está vazia
        return None
    minimo = lista[0]  # assume o primeiro como menor
    for numero in lista:
        if numero < minimo:
            minimo = numero
    return minimo