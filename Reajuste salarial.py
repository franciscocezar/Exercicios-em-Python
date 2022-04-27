salario = float(input('Qual é o salário do funcionário? R$ '))
reajuste = salario + (salario * 15 / 100)

print(f'Salário atual do funcionário: R${salario:.2f} \nSalário com reajuste de 15%: R$ {reajuste}')
