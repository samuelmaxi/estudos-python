"""
Interável -> str, range, etc
Interador -> quem sabe entregar um valor por vez
next -> me entregao próximo valor
inter -> me entregue seu iterador 
"""

texto = 'Luiz' # iterável
# iterador = iter(texto) # iterador 

# while True:
#     try:
#         print(next(iterador))
#     except StopIteration:
#         break
        #|
        #|
        #v
for letra in texto:
    print(letra)



# numeros = range(0,100, 2)

# for numero in numeros:
#     print(numero)
