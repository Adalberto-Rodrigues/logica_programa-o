#exercicio_03
"""Escreva um programa que receba o salário de uma pessoa e diga quanto ela pagará apenas de Imposto de Renda. Considere as seguintes faixas de incidência do imposto:"""

#até R$ 2.259,20 – isento;
#de R$ 2.259,21 a R$ 2.826,65 – 7,5%;
#de R$ 2.826,66 a R$ 3.751,05 – 15%
#de R$ 3.751,06 a 4.664,68 – 22,5%; e
#acima de R$ 4.664,68 – 27,5%.

print("Resposta")
n = int(input('quanto você ganha? '))
if n <= 2259.20 :
    print('insento')
elif n >= 2259.21 and n <= 2826.65:
    print( 'pagará 7,5%')
elif n >= 2826.66 and n <= 3751.05:
    print( 'pagará 15%')
elif n >= 3751.06 and n <= 4664.68:
    print( 'pagará 22,5%')
else:
    n > 4664.68 
    print( 'pagará 27,5%')

