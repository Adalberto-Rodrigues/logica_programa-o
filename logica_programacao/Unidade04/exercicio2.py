#exercicio_02
"""No mundo de The Witcher, criaturas diferentes apresentam características únicas.
Baseado nas pistas abaixo, escreva um programa que identifique o tipo de criatura que
Geralt está enfrentando:"""

#Se o monstro aparece à noite, tem garras e evita prata, é um Lobisomem.
#Se aparece durante o dia ou à noite, é rápido e ataca em grupo, é um Nekker.
#Se aparece em qualquer horário, não tem olhos, mas imita vozes humanas, é um Mímico.
#Se nenhuma dessas combinações for satisfeita, o programa deve imprimir: "Criatura desconhecida. Prepare-se para o pior.
#O usuário irá informar:

"""horario → dia ou noite
    caracteristica1 → ex: garras, rápido, não tem olhos, etc.
    caracteristica2 → ex: evita prata, ataca em grupo, imita vozes humanas, etc."""

print("Resposta")
# Perguntas para identificar as características
horario = input("O monstro aparece à noite, durante o dia ou em qualquer horário? ").strip().lower()
tem_garras = input("O monstro tem garras? (sim/não) ").strip().lower()
evita_prata = input("O monstro evita prata? (sim/não) ").strip().lower()
eh_rapido = input("O monstro é rápido? (sim/não) ").strip().lower()
ataca_em_grupo = input("O monstro ataca em grupo? (sim/não) ").strip().lower()
imita_vozes = input("O monstro imita vozes humanas? (sim/não) ").strip().lower()
tem_olhos = input("O monstro tem olhos? (sim/não) ").strip().lower()
# Verificação das condiçõesnoite
if horario == "noite" and tem_garras == "sim" and evita_prata == "sim":
    print("É um lobisomem")
elif (horario == ["dia", "noite"] and eh_rapido == "sim" and ataca_em_grupo == "sim" and imita_vozes == "sim"):
    print("É um Nekker")
elif (horario == "qualquer horário" and tem_olhos == "não" and imita_vozes == "sim"):
    print("É um Mirro")
else:
    print("Criatura desconhecida. Prepare-se para o pior.")
