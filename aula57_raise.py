# raise - lançando exceções (erros)
def nao_aceitar_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você esta tentando dividir por zero')


def dev_ser_int_float(n):
    tipo_n = type(n)

    if not isinstance(n, (float, int)):
        raise TypeError(f'{n} deve ser int ou float. '
                        f'"{tipo_n.__name__}" enviado')
    return True


def divide(n, d):
    dev_ser_int_float(n)
    dev_ser_int_float(d)
    nao_aceitar_zero(d)

    return n / d


print(divide(0, '0'))
