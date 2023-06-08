# Try, except, else e finally

# a = 18
# b = 0
# c = a/b

# try:
#     a = 18
#     b = 0
#     # print(b[0])
#     # print('Linha 1'[1000])
#     c = a/b
#     print('Linha 2')

# except ZeroDivisionError as e:
#     print(e.__class__.__name__)
#     print(e)
# except NameError:
#     print('Nome b não está definido.')
# except (TypeError, IndexError) as error:
#     print('Erro de tipos + erro de index')
#     print('MSG: ', error)
#     print('Nome: ', error.__class__.__name__)
# except Exception:
#     print('Erro desconhecido')

# print('CONTINUAR')


try:
    print('Abril')
except:
    print('Dividiu zero')
else:
    print('Não deu erro')
finally:
    print('Fechou')
