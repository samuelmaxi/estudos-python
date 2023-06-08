# Empacotamento desempacotamento de dicionarios

a, b = 1, 2
a, b = b, a
# print(a, b)

# (a1, a2), (b1, b2) = pessoa.items()
# print(f'{a1}: {a2}\n{b1}: {b2}')

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Sousa',
}
dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoa_completa = {**pessoa,
                   **dados_pessoa}

print(pessoa_completa)

# args e kwargs
# kwargs - keyword arguments (argumentos nomeados)
