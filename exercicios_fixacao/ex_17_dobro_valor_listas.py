def dobrar_valores(lista):
    lista_2 = []
    for valor in lista:
        lista_2.append(valor * 2)
        
    return lista_2

lista = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

nova_lista = dobrar_valores(lista)
print(nova_lista)