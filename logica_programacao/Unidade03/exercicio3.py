#exercicio_03
"""Faça um Programa que pergunte ao usuário quanto você ganha por hora e 
o número de horas trabalhadas por dia, considerando que se trabalha 5 dias 
por semana. Calcule e mostre o total do seu salário ao mês."""
print("esposta")
valor_hora = float(input("digite quanto você ganha por hora:"))
horas_dia = float(input("digite quantas horas voce trabalha por dia:"))
salario_mensal = valor_hora * horas_dia * 5 * 4
print(f"vovê alcancou um valor de {salario_mensal} reais este mês")
