def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def divisao(n1, n2):
    return n1 / n2

def multiplicacao(n1, n2):
    return n1 * n2

operacao = ['adição', 'subtração', 'divisão', 'multiplicação']
operacao = input('Digite qual o percação você quer (adição, subtração, divisão ou multiplicação): ')

if operacao == 'adição':
    valor1 = float(input('Digite um valor: '))
    valor2 = float(input('Digite outro um valor: '))
    resultado = soma(valor1, valor2)
    print(f'{resultado= }')

elif operacao == 'subtração':
    valor1 = float(input('Digite um valor: '))
    valor2 = float(input('Digite outro um valor: '))
    resultado = subtracao(int(valor1), int(valor2))
    print(f'{resultado=}')

elif operacao == 'divisão':
    valor1 = float(input('Digite um valor: '))
    valor2 = float(input('Digite outro um valor: '))
    resultado = divisao(int(valor1), int(valor2))
    print(f'{resultado=}')

elif operacao == 'multiplicação':
    valor1 = float(input('Digite um valor: '))
    valor2 = float(input('Digite outro um valor: '))
    resultado = multiplicacao(int(valor1), int(valor2))
    print(f'{resultado=}')

else:
    print('Erro nenhuma operação encontrada!')  