# verb = int(str('Verbo: '))
# number = int(str('Number: '))
# candidate = int(str('Candidate: '))
# pluralModifier = int(str('Verbo: '))

import random #biblioteca usada

pessoas = [ 'Wandson Ramos','Gabriel Cesar','Caio Rego' ]

def calcular_impar_par():
    count = random.randint(1, 100)
    return count

contador = calcular_impar_par()

def frase(verb, pluralModifier):
    return (f'There {verb} '+pessoas [ random.randrange ( len ( pessoas ))] + f'{pluralModifier}')

if contador % 2==0: # contador
    verb = 'are'
    pluralModifier = 's'
    palavras = frase(verb, pluralModifier)
else:
    verb = 'is' 
    pluralModifier = ''
    frase(verb, pluralModifier)

print(frase(verb, pluralModifier))
