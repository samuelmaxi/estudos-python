import random 

lista_1 = [random.randrange(0, 20) for i in range(10)]
lista_2 = [random.randrange(0, 20) for i in range(10)]

lista_semelhantes = []

i =0
for numero in lista_1:
    if numero in lista_2:
        lista_semelhantes.append(numero)

print(lista_1)
print(lista_2)
print(lista_semelhantes)
