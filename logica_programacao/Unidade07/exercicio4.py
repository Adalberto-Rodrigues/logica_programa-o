#exercicio_04
"""Crie uma função chamada analisa_lista que recebe uma lista de números como parâmetro e retorna um dicionário contendo a soma de todos os números, a média dos números e o maior e o menor número da lista."""
print("Resposta")
def analisa_lista(lista):
    if not lista:
        return {
            "soma": 0,
            "media": 0,
            "maior": None,
            "menor": None
        }
    
    soma = sum(lista)
    media = soma / len(lista)
    maior = max(lista)
    menor = min(lista)

    return {
        "soma": soma,
        "media": media,
        "maior": maior,
        "menor": menor
    }

# Exemplo de uso:
entrada = input("digite numeros separados por virgulas e espaço:")

#converte a string em lista inteiros
lista_numeros =[int(x.strip()) for x in entrada.split(",")]

print("Os resultados são:", analisa_lista(lista_numeros))