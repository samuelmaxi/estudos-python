# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicador(*args):
    valor = 1
    for numero in args:
        valor *= numero

    return valor


multiplicados = multiplicador(1, 2, 3, 4, 5, 6)
print(multiplicados)


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def calcular_impar_par(numero):
    if numero % 2 == 0:
        return 'O número é par'
    return 'O número é impar'

 
print(calcular_impar_par(23))
print(calcular_impar_par(12))
print(calcular_impar_par(56))