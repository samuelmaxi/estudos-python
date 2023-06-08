# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# def zipper(names_list, acronyms_list):
#     intervalo = min(len(names_list), len(acronyms_list))

#     return [
#         (names_list[i], acronyms_list[i]) for i in range(intervalo)
#     ]
#     # new_list = list(zip(acronyms_list, names_list))   MINHA RESPOSTA
#     # return new_list

# new_list_states = zipper(list_name_states, list_acronyms_states)
from itertools import zip_longest

list_name_states = ['Salvador', 'Ubatuba', 'Belo Horizonte']
list_acronyms_states = ['BA', 'SP', 'MG', 'RJ']


print(list(zip(list_name_states, list_acronyms_states)))
print(list(zip_longest(list_name_states, list_acronyms_states, fillvalue='SEM CIDADE')))
