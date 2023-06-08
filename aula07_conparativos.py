def comparadorValores (v1, v2):
    if v1 > v2:
        print(f'{v1= } é maior que o {v2= }')
    elif v2 > v1:
        print(f'{v2= } é maior que o {v1= }')
    else:
        print(f'o {v1} e o {v2} tem o mesmo valor')


valor1 = input('Digite um valor: ')
valor2 = input('Digite outro valor: ')

resultado = comparadorValores(valor1, valor2)
