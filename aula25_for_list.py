"""
for in com listas
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# i = 0
# for nome in lista:
                                # MINHA RESPOSTA
#     print(f'{i} {nome}')  
#     i += 1

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))