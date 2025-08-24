#exercicio_04
"""Escreva um programa que peça ao usuário um número entre 1 e 100. O programa deve verificar:"""

#Se o número é divisível por 3, exiba "Número divisível por 3".
#Se o número é divisível por 5, exiba "Número divisível por 5".
#Se o número é divisível por 3 e 5, exiba "Número divisível por 3 e por 5.".
#Caso contrário, exiba "Número comum".

print("Resposta")
print('verificação do número')
# Solicita um número ao usuário
numero = int(input("Digite um número entre 1 e 100: "))
# Verifica se está no intervalo permitido
if 1 <= numero <= 100:
    if numero % 3 == 0 and numero % 5 == 0:
        print("Número divisível por 3 e por 5")
    elif numero % 3 == 0:
        print("Número divisível por 3")
    elif numero % 5 == 0:
        print("Número divisível por 5")
    else:
        print("Número comum")
else:
    print("Número fora do intervalo permitido!")

