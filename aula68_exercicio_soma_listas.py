"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""
from itertools import zip_longest

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
sum_list = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]

new_sum_list = []
little_list = min(lista_a, lista_b)

i = 0
for num in little_list:
    valuer = num + lista_a[i]
    new_sum_list.append(valuer)
    i += 1


print(lista_a)
print(lista_b)
print(new_sum_list)
print(sum_list)
