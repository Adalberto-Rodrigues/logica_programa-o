#exercicio_10
"""Crie dois conjuntos: alunos_python e alunos_java. Coloque 3 nomes em cada e:

° Mostre os alunos que fazem as duas linguagens.
° Mostre os alunos que fazem só Python.
° Mostre todos os alunos (sem repetição)."""
print('Respostas')
alunos_python = {'jonne','jax','joe'}
alunos_java = {'joe','cloe','lala'}
ambos = alunos_python & alunos_java
so_python = alunos_python - alunos_java
todos = alunos_python | alunos_java
print('fazem os dois {}'.format(ambos))
print('fazem os dois {}'.format(so_python))
print('fazem os dois {}'.format(todos))