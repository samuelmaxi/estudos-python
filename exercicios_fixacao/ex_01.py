lista_numb = (range(10))

lista_quadratica = []
# lista_quadratica = [x ** 2 for x in lista_numb] for na mesma linha

for numero in lista_numb:
    lista_quadratica += [numero ** 2]

print(lista_quadratica)