# isinstance - para saber se objetos é de determinado tipo

lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'}
]

for item in lista:
    if isinstance(item, set):
        print('set')
        item.add(5)
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        print('STR')
        print(item.upper())

    elif isinstance(item, bool):
        print('BOOL')
        print(item)

    elif isinstance(item, (int, float)):
        print('NUMB')
        print(item, item * 2)

    else:
        print('OUTRO')
        print(item)
