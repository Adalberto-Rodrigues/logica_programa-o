#exercicio_06
"""Escreva um programa que peça ao usuário para digitar a temperatura em Fahrenheit e converta para Celsius e Kelvin, imprimindo o resultado na tela."""
print("Resposta")
fahrenheit = float(input('digite a temperatura em fahrenheit:'))
celsius = (fahrenheit - 32) * 5/9
kelvin = celsius + 273.15
print(f'Temperatura em Celsius:{celsius: .2f} ºC')
print(f'Temperatura em Kelvin:{kelvin: .2f} ºK')
