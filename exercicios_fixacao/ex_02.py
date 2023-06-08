lista_numeros = (range(101))

lista_pares = []
lista_impares = []

i=0
for numero in lista_numeros:
    if numero %2==0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
print(f'Lista de numeros pares:\n{lista_pares}')
print(f'Lista de numeros impares:\n{lista_impares}')
