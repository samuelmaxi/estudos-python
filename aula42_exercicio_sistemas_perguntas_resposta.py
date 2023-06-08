"""
Exercício de perguntas e respostas
"""
# import os

# def questionario(questao, lista_perguntas):
#         if questao == 1:
#             os.system('clear')

#             print(lista_perguntas[0]['Pergunta'])
#             print(lista_perguntas[0]['Opções'])

#             def respostas(resposta_usuario):
#                     if str(resposta_usuario) in lista_perguntas[0]['Resposta']:
#                         print('Acertou')
#                     else:
#                         print('Errou')

#         if questao == 2:
#             os.system('clear')

#             print(lista_perguntas[1]['Pergunta'])
#             print(lista_perguntas[1]['Opções'])

#             def respostas(resposta_usuario):
#                     if str(resposta_usuario) in lista_perguntas[1]['Resposta']:
#                         print('Acertou')
#                     else:
#                         print('Errou')

#         if questao == 3:
#             os.system('clear')

#             print(lista_perguntas[2]['Pergunta'])
#             print(lista_perguntas[2]['Opções'])

#             def respostas(resposta_usuario):
#                     if str(resposta_usuario)in lista_perguntas[2]['Resposta']:
#                         print('Acertou')
#                     else:
#                         print('Errou')

#         return respostas


lista_de_perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5', '6'],
        'Resposta': '4'
    },
    {
        'Pergunta': 'Quanto é 5 * 5?',
        'Opções': ['5', '255', '55', '25', '45'],
        'Resposta': '25'
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '3', '5', '1', '2'],
        'Resposta': '5'
    },
]
qtd_acertos = 0
for pergunta in lista_de_perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i}) {opcao}')
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    if acertou:
        qtd_acertos += 1
        print('Acertou')
    else:
        print('Errou')

print('Você acertou: ', qtd_acertos)
print('de', len(lista_de_perguntas), 'perguntas')
