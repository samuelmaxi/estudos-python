# Generator expression, Iterables e Iterators em Python
import sys

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # ter __iter__ e __next__

generator = (n for n in range(10000))
lista = [n for n in range(10000)]

print(sys.getsizeof(generator))
print(sys.getsizeof(lista))
