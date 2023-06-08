#Desempacotamento em chamadas
#de métodos e função

string = 'ABC'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

# p, b, *_, ap, u = lista
# print(p, u, ap)

print(*lista, sep=', ')