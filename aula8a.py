import math
import random

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz quadrada de {num} é {math.ceil(raiz)}')
print(f'A raiz quadrada de {num} é {math.floor(raiz)}')
print(f'A raiz quadrada de {num} é {raiz:.2f}')

print()
n2 = random.randint(1, 10)
print(n2)
