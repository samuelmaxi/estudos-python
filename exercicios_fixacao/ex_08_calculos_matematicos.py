def verificador_de_numeros(lista_numeros):
    maior = lista_numeros[0]
    for numero in lista_numeros:
        if numero > maior:
            maior = numero

    return maior

lista_numeros = [5, 7, 2, 4, 9, 1]

maior_numero = verificador_de_numeros(lista_numeros)
print(maior_numero)
