"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista_compras = []
i = 0
quantidade_itens = len(lista_compras)
while True:
    print('Qual das funções abaixo quer realizar?\n1-Inserir\t2-Apagar\t3-Listar itens')
    resposta = int(input('Realizar a função de: '))
    try:
        if resposta == 1:
            quantidade = int(input('Quantos itens quer adicionar: '))
            os.system('clear')

            for i in range(quantidade):
                item = input('Qual item sera adicionado:')
                lista_compras.append(item)
            
            resposta_sair = input('Deseja sair?')

        elif resposta == 2:
            quantidade = int(input('Quantos itens deseja apagar: '))
            os.system('clear')

            for i in range(quantidade):
                    indices = int(input('Qual o indice do item que vc deseja apagar: '))
                    del lista_compras[indices]

            resposta_sair = input('Deseja sair?')
        
        elif resposta == 3:
            os.system('clear')
            if len(lista_compras) < 1:
                print('Lista vazia')
                continue
            for indice, nome in enumerate(lista_compras):
                print(indice, nome)
           
            resposta_sair = input('Deseja sair?')

        if resposta_sair.lower() == 'sim':
            os.system('clear')
            print('Sua lista esta assim: ')

            for indice, nome in enumerate(lista_compras):
                print(indice, nome)
            break

        else:
            os.system('clear')
            continue
    except ValueError:
        print('Não foi encontrado essa opção dentro das funções')
        continue
    except IndexError:
        print('Índice não existe na lista')
    except NameError:
        print('Só digite uma opção por vez')
    except Exception:
        print('Erro desconhecido')

print('Sua lista foi finalizada')
