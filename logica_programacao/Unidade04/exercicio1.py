#exercicio_01
"""Escreva um programa que leia o nome de um dia da semana e verifique se é um dia útil ou um dia de fim de semana. Caso seja um dia útil, imprima "Dia útil". Caso seja um dia de fim de semana, imprima "Fim de semana"."""
print("Resposta")
# Solicita o nome do dia da semana
dia = input("Digite o nome de um dia da semana: ").strip().lower()
# Verifica o tipo de dia
if dia in ["sábado", "sabado", "domingo"]:
    print("Fim de semana")
elif dia in ["segunda", "terça", "terca", "quarta", "quinta", "sexta"]:
    print("Dia útil")
else:
    print("Dia inválido")


