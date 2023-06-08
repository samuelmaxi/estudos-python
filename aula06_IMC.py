def imc(peso, altura):
    return peso / (altura * altura)

nome = 'Samuel'
altura = 1.80
peso = 73
IMC = imc(peso, altura)
print(f'{nome} tem {altura} de altura,\npeso {peso} quilos e seu IMC é \n{IMC:.2f}') # ou {round(IMC, 2)} para colocar ponto flutuante
