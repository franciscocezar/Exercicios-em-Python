nome = str(input('Digite o seu nome completo: ')).strip()

dividido = nome.split()

print('Analisando seu nome..')

print(f'Seu nome em letras maiúsculas é: {nome.upper()}.')
print(f'Seu nome em letras minúsculas é: {nome.lower()}.')
print('Seu nome tem ao todo ', len(nome) - nome.count(' '), 'letras.')
print('Seu primeiro nome é', dividido[0], ', e tem ', len(dividido[0]), 'letras.')

