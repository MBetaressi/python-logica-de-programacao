import math
num = int(input("Digite um número: "))
raiz = math.sqrt(num)
print(f"A raiz quadrada de {num} é igual a {raiz:.2f}")
print(f"A raiz qudrada de {num} é igual a {math.ceil(raiz)}")
print(f"A raiz qudrada de {num} é igual a {math.floor(raiz)}")

print('\n')

from math import sqrt, floor
num = int(input("Digite um número: "))
raiz = sqrt(num)
print(f"A raiz quadrada de {num} é igual a {math.floor(raiz)}")

print('\n')

from random import randint
num = randint(1, 10)
print(num)
