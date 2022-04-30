# Separando dígitos de um número

num = int(input('Informe um número: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print()
print(f'O número {num} contém:\n{unidade} como unidade'
      f'\n{dezena} como dezena \n{centena} como centena'
      f'\n{milhar} como milhar')
