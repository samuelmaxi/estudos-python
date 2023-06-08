"""
Iterando string com while
"""

nome = 'Samuel Máximo'

tamanho_nome = len(nome)

print(nome)
print(tamanho_nome)

print(nome[4])
novo_nome = '*'
indice =0


while indice < tamanho_nome:
    novo_nome += nome[indice]+ '*'
    indice+=1

print(novo_nome)