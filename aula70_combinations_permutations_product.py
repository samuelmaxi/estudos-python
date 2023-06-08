# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


people = ['João', 'Joana', 'Luiz', 'Letícia']
t_shirt = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'tecido', 'linha', 'malha'],
]


# print_iter(combinations(people, 2))
# print_iter(permutations(people, 2))
print_iter(product(*t_shirt))
