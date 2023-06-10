# Problemas dos parâmetros mutaveis em funções Python


def add_clients(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


lista1 = []

clientes1 = add_clients("luiz", lista1)
add_clients("Joana", clientes1)
print(clientes1)

clientes2 = add_clients("Helena")
add_clients("Jao", clientes2)
print(clientes2)
