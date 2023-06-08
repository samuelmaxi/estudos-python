lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))

lista = [
    (x, y, z)
    for x in range(3)
    for y in range(3)
    for z in range(3)
    if z != x and z != y
]

lista = [
    [letra for letra in 'Luiz']
    for x in range(3)
]

print(lista)
