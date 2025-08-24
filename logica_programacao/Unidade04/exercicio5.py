#exercicio_05
""" Crie um programa que receba uma senha e verifique sua validade com base nas seguintes condições:"""

#Deve ter pelo menos 8 caracteres.
#Deve conter pelo menos uma letra maiúscula.
#Deve conter pelo menos um número.
#Não pode conter espaços em branco.

print("Resposta")
print('digite uma senha com pelo menos 8 caracteres, contendo pelo menos uma letra maiúscula, um número e não pode conter espaços em branco')
senha = input('digite uma senhar forte: ')
#Verificações
tem_8_caracteres = len(senha) >= 8
tem_maiuscula = any(c.isupper() for c in senha)
tem_numero = any(c.isdigit() for c in senha)
nao_tem_espaco = " " not in senha
# Validação
if tem_8_caracteres and tem_maiuscula and tem_numero and nao_tem_espaco:
    print("Senha válida!")
else:
    print("Senha inválida. Verifique os seguintes critérios:")
    if not tem_8_caracteres:
        print("- Deve ter pelo menos 8 caracteres.")
    if not tem_maiuscula:
        print("- Deve conter pelo menos uma letra maiúscula.")
    if not tem_numero:
        print("- Deve conter pelo menos um número.")
    if not nao_tem_espaco:
        print("- Não pode conter espaços em branco")
        