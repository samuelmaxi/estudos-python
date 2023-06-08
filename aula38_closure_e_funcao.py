"""
Closure e funções que retorna outras funções
"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Maria', 'Luiz', 'Tiago', 'Samuel']:
    print(falar_boa_noite(nome))
    print(falar_bom_dia(nome))