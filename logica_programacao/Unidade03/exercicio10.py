#exercicio_10
"""Escreva um programa que receba duas frases SEPARADAMENTE e imprima de maneira invertida, em adição, troque as letras A por *."""
print("Resposta")
frase1 = input('digite a primeira frase? ')
frase2 = input('digite a segunda frase? ')
frase1_modificada = frase1[::-1].replace('a', '*').replace('A', '*')
frase2_modificada = frase2[::-1].replace('a', '*').replace('A', '*')
print('frase 1 modificada:',frase1_modificada)
print('frase 2 modificada:',frase2_modificada)
