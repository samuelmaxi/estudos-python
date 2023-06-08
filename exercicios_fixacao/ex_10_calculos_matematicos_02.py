def somar_numeros_naturais(numero):
    soma = 0
    for numero in range(1, numero +1):
        soma += numero

    return soma

num = int(input('Digite um numero inteiro: '))
res= somar_numeros_naturais(num)

print(f'A soma dos numeros: {res}')