# count é um iterador sem fim (itertools)
from itertools import count

c1 = count()
r1 = range(10)

for i in c1:
    if i > 100:
        break
    print(i)

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
