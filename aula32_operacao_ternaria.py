"""
Operação ternária (condicional de um linha)
<valor> if <condicao> else <outro valor>
"""
# condicao = 10 == 11
# variavel = 'Valor'if condicao else 'Outra valor'
# print(variavel)

digito = 9 # > 9 = 0
# novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)