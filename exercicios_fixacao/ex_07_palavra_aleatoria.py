"""
Escreva um programa que gere uma string aleatória a partir de uma lista
de caracteres específicos e crie uma nova string que seja a concatenação
dessas strings aleatórias.
"""
import random

caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',\
           'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',\
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def gerador_de_palavras(quantidade_letras, palavra):
    palavra_gerada = ''.join(random.choices(palavra, k= quantidade_letras))
    return palavra_gerada

quantidade_letras = int(input('Digite a quantidade de letras que vc quer na sua palavras: '))


palavra_gerada = gerador_de_palavras(quantidade_letras, caracteres)
print(palavra_gerada)