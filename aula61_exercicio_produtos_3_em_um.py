import copy
from dados import produtos

# copy, sorted, produtos.sort
# Exercícios


# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

new_produtos = copy.deepcopy(produtos)
# print(*produtos, sep='\n')

i = 0
for index in produtos:
    # print(produtos[i]['preco'])
    increase = (produtos[i]['preco'] * 0.1)
    new_produtos_value = round(produtos[i]['preco'] + increase, 2)
    new_produtos[i]['preco'] = new_produtos_value
    i += 1


# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
# Valor decrescente em referente ao nome
for i in new_produtos:
    new_produtos_orderly = sorted(
        copy.deepcopy(new_produtos),
        key=lambda x: x['nome'],
        reverse=True)

print('Organização da tabala em ordem decrescente em referente ao nome\n')
for produto in new_produtos_orderly:
    print(produto)

print()


# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
# Valor decrescente em referente ao preço
for i in new_produtos:
    new_produtos_orderly = sorted(
        copy.deepcopy(new_produtos),
        key=lambda x: x['preco'],
        reverse=False)

print('Organização da tabala em ordem crescente em referente ao preço\n')
for produto in new_produtos_orderly:
    print(produto)

print('---'*10)
print(*produtos, sep='\n')
