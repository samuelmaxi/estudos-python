"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = 'Perfume'.lower()
tentativas = 0
letras_acertadas = ''

while True:
    
    letra_digitada = input('Digite uma letra: ')
    tentativas += 1
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print(f'Palavra formada:{palavra_formada}')


    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('Você conseguiu acertar a palavra secreta'.upper())
        print(f'Quantidade de tentativas: {tentativas}x')
        print(f'A palavra secreta é {palavra_secreta.upper()}')
        tentativas = 0
        letras_acertadas = ''
    

# for letra in palavra_secreta: C/E C
#     letra = input('Digite uma letra: ') C
    
#     if letra == palavra_secreta[i]:
#         print('Letra correta')
#         palavra_adivinhada += letra + '*'
#         print(palavra_adivinhada)
#         i+=1
#     elif i != 0:
#         print(f'{letra}')
#     else:
#         print('Letra errada"')
#         print('*'*len(palavra_secreta))


# print(palavra_secreta)

