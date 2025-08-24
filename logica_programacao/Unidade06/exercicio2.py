# Exercicio_02
"""Escreva um programa que leia os nomes e as notas de 5 alunos e armazene esses dados em um dicionário, onde a chave seja o nome do aluno e o valor seja a nota. Depois:"""
#a) Exiba de maneira organizada o nome e a nota de cada aluno.
#b) Calcule e exiba de maneira organizada a média da turma. 
#c) Identifique e exiba o nome do aluno de maior nota.

print("Resposta")
alunos = {}

for i in range(5):
    nome = input(f"Digite o nome do {i+1}º aluno: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos[nome] = nota

# Exibir nome e nota de cada aluno
print("\n--- Lista de Alunos e Notas ---")
for nome, nota in alunos.items():
    print(f"{nome}: {nota:.2f}")

# Calcular e exibir a média da turma
media = sum(alunos.values()) / len(alunos)
print(f"\nMédia da turma: {media:.2f}")

# Identificar o aluno com maior nota
aluno_maior_nota = max(alunos, key=alunos.get)
print(f"\nAluno com maior nota: {aluno_maior_nota} ({alunos[aluno_maior_nota]:.2f})")