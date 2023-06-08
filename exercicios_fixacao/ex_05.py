def contador_letras(lista):
    anterior = 0
    for indice in lista:
        if len(indice) >= len(lista):
            palavrao = indice
            anterior += 1
    return palavrao

lista_palavras = ['Maria', 'Helena', 'Luiz']

maior_palavra = contador_letras(lista_palavras)

print(maior_palavra)

#QUESTAO INCOMPLETA PARA TERMINAR