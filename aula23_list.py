"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimento reutilizáveis - índices e fatiamento
Métodos úteis: 
            append - Adiciona um item ao final
            insert - Adiciona um item no índice escolhido
            pop - Remove do final ou do índice escolhido
            clear - Limpa a lista
            extend - Estende a lista
            del - Apaga um índice
            + - concatena listas

Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

#    01234
#   -54321

# lista = [] -> lista vazia 
# print(bool([])) # falsy

# del lista[-1] # ultimo item da lista
# lista.clear()
# lista.insert(0, 5) # primeiro é o indice e o segundo o valor que vai colocar

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)

