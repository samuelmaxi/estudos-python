# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def calcular(multiplicador):
    def multiplcar(numero):
        res_multiplicacao = numero * multiplicador
        return f'Numero {numero} multiplicado por {multiplicador}: {res_multiplicacao}'

    return multiplcar

duplicador_valor = calcular(2)
triplicar_valor = calcular(3)
quadruplicar_valor = calcular(4)
quintuplicar_valor = calcular(5)

print(duplicador_valor(25))
print(triplicar_valor(25))
print(quadruplicar_valor(25))
print(quintuplicar_valor(25))