"""Calculadora com while"""

while True:
    try:
        valor_1 = float(input('Digite um valor: '))
        valor_2 = float(input('Digite um valor: '))
    except:
        print('Você digitou valores inválidos...')
        continue

    lista_operadores = ['+', '-', '*', '/']
    seletor_operadores = input('Escolha o operador ("+", "-", "*", "/"): ')

    soma = seletor_operadores == '+'
    subtração = seletor_operadores == '-'
    multiplicacao = seletor_operadores == '*'
    divisao = seletor_operadores == '/'

    if soma:
        print(f'{valor_1} {seletor_operadores} {valor_2} = ', valor_1 + valor_2)
        
    elif subtração:
        print(f'{valor_1} {seletor_operadores} {valor_2} = ', valor_1 - valor_2)

    elif multiplicacao:
        print(f'{valor_1} {seletor_operadores} {valor_2} = ', valor_1 * valor_2)

    elif divisao:
        print(f'{valor_1} {seletor_operadores} {valor_2} = ', valor_1 / valor_2)
    
    else:
        print('Não foi identificado nenhum operador da lista, ou você digitou mais de um operador...')
        continue

    opcao_sair = input('Se deseja [S]air digite "S": ').lower().startswith('s')

    if opcao_sair is True:
        break
    else:
        print('Você ira voltar ao inicio...')
        continue

print('Você saiu da calculadora')