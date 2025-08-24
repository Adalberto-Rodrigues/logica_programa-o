#exercicio_07
"""Número de Vogais Peça ao usuário para inserir uma frase.
Usando um laço for conte e exiba quantas vogais existem na frase.
Lembre de verificar a documentação do módulo String em busca de métodos que
facilitem a verificação da letra ser vogal."""

print("Resposta")

import string
frase = input("Digite uma frase: ")

vogais = "aeiouAEIOU"

contador = 0

for letra in frase:
    if letra in vogais:
        contador += 1

print(f"\nA frase contém {contador} vogais.")