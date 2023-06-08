# Introdução às Generator Functions em Python
# generator = (n for n in range(10000))
# Yield from

def gen1():
    yield 1
    yield 2
    yield 3


def gen2():
    yield from gen1()
    yield
