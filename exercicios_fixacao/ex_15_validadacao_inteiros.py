def varificador(numero):
    par = numero % 2 == 0
    
    if par:
        return  f'{numero} é par e não é estranho'
    
    return f'{numero} é impar e é estranho'


print(varificador(3))
print(varificador(24))