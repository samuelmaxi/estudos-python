# Aqui vou fazer as questões do site da beecrownd


# Escreva um programa que calcule o fatorial de um número usando um loop for.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        fac = n * factorial(n - 1)
        return fac


print(factorial(4))
