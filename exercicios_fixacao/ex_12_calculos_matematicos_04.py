"""
Escreva uma função que calcule o fatorial de um número.
"""

def fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

num = int(input("Digite um número: "))
print("O fatorial de", num, "é", fatorial(num))