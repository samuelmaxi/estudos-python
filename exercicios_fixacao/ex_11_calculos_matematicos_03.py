"""
Escreva uma função que verifique se um número é primo ou não
"""

def verificar_num_primos(num):
    if num <= 1:
        return False
    for numero in range(2, num):
        if num % numero == 0:
            return False
        
    return True

# lista de numeros primos:  2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
# 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

numero = int(input('Digite um valor para saber se ele é primo ou não: '))
resultado = verificar_num_primos(numero)

if verificar_num_primos(numero):
    print(f'O número {numero} é primo')
else:
    print(f'{numero} Não é primo')
