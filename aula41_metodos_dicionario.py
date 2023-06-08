# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

import copy
pessoa = {
    'nome' : 'Samuel',
    'sobrenome' : 'Araújo',
    'idade' : 19,
    # 'altura' : 1.8,   
}
pessoa.setdefault('idade', None)

print(pessoa['idade'])
 
copia_pessoa = copy.deepcopy(pessoa)

copia_pessoa['nome'] = 'Pedro'

print(pessoa)
print(copia_pessoa)

# print(len(pessoa))
# print(tuple(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.values()))



# for chave in pessoa.items():
#     print(chave)

# for chave, valor in pessoa.items():
#     print(chave, valor)