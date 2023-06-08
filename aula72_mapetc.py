from functools import partial
from types import GeneratorType

# map - para mapear dados


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


def aumentar_porcentage(valor, porcentagem):
    return round(valor * porcentagem, 2)


aumentar_dez_porcento = partial(aumentar_porcentage, porcentagem=1.1)

# novo_produtos = [
#     {**p, 'preco': aumentar_dez_porcento(p['preco'])} for p in produtos
# ]


def muda_preco_de_produto(produto):
    return {**produto, 'preco': aumentar_dez_porcento(produto['preco'])}


novo_produtos = map(
    muda_preco_de_produto, produtos
)

novo_produtos = (x for x in produtos)

print_iter(produtos)
print_iter(novo_produtos)

print(isinstance(novo_produtos, GeneratorType))

print(
    list(map(
        lambda x: x*3,
        [1, 2, 3, 4, 5, 6]
    ))
)
