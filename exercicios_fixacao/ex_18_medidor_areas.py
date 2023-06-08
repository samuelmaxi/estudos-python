"""
Voltar nesse exercício quando estiver estudando objeto
"""

def escreva(texto):
    linhas = '----' * len(texto)
    print(f'{linhas}\n{texto.center(len(linhas))}\n{linhas}')
    return linhas

def area(altura, largura):
    objeto = altura * largura
    return objeto                             #Exercicios de função


quadrado = area(4.5, 8)

print(quadrado)

print('------------------------')




titulo = 'Ola mundo'
linhas = escreva(titulo)

# print(linhas)
# print(titulo.center(len(linhas))) outra forma de fazer
# print(linhas)