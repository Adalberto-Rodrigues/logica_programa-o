#exercicio_09
"""Escreva um programa que leia uma string contendo letras 
de uma frase inclusive os espaços em branco e retire os espaços
 em branco e depois escreva a string resultante."""
print("Resposta")
frase = input('digite uma frase:')
frase_sem_espaco = frase.replace(" ","")
print(f"Frase sem espaço. {frase_sem_espaco}")
