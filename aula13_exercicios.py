"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# numero = input('Digite um numero inteiro: ')

# if numero.isdigit():
#     print('O valor é inteiro')
#     valor_inteiro = int(numero)
#     valor_par_impar = valor_inteiro % 2 ==0
#     valor_par_impar_text = 'ímpar'
    

#     if valor_par_impar:
#         valor_par_impar_text = 'par'

#     print(f'O numero {valor_inteiro} é {valor_par_impar_text}')
    
# else:
#     print('O numero não é inteiro')

#OUTRO MODO DE RESOLVER

# try:
#     print('O valor é inteiro')
#     valor_inteiro = int(numero)
#     valor_par_impar = valor_inteiro % 2 ==0
#     valor_par_impar_text = 'ímpar'
    

#     if valor_par_impar:
#         valor_par_impar_text = 'par'

#     print(f'O numero {valor_inteiro} é {valor_par_impar_text}')
    
# except:
#     print('O numero não é inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# try:
#     horario = int(numero)
#     manha = horario >= 0 and horario <= 11
#     tarde = horario >= 12 and horario <= 17
#     noite = horario >= 18 and horario <= 23

    
#     if manha:
#         print('Bom dia!')

#     if tarde:
#         print('Boa tarde!')

#     if noite:
#         print('Boa noite!')

# except:
#     print('Digite numeros inteiros')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

primeiro_nome = input('Digite seu primeiro nome: ')
tamanho_nome = len(primeiro_nome)
nome_curto = len(primeiro_nome) <= 4
nome_normal = len(primeiro_nome) >=5 and len(primeiro_nome) <=6
nome_grande = len(primeiro_nome) > 6

if tamanho_nome > 1:
    if nome_curto:
        print('Seu nome é curto')

    elif nome_normal:
        print('Seu nome é normal')

    else:
        print('Seu nome é muito grande')

else:
    print('Digite mais letras')
