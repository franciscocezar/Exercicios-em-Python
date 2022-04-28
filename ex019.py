import random

a1 = input('Digite o nome de um aluno: ')
a2 = input('Digite o nome de outro aluno: ')
a3 = input('Digite o nome de mais um aluno: ')
a4 = input('Digite o nome do último aluno: ')

lista = [a1, a2, a3, a4]

print(f'O aluno escolhido foi {random.choice([a1, a2, a3, a4])}')
