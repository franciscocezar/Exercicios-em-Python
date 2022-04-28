# Manipulação de texto

frase = 'Tente. Fracasse. Não importa. Tente de novo. Fracasse de novo. Fracasse melhor.'
dividido = frase.split()
print()
print(frase)
print(f'A frase tem {len(frase)} caracteres.')

print()
print(f'Na frase tem a palavra "melhor"?')
print('melhor' in frase)

print()
print(dividido)
print(f'Há {len(dividido)} listas.')

print()
print(' ;) '.join(dividido))

print()
print("""Nada é impossível de mudar
Desconfiai do mais trivial, na aparência singelo.
E examinai, sobretudo, o que parece habitual.
Suplicamos expressamente: não aceiteis o que é de 
hábito como coisa natural, pois em tempo de desordem sangrenta, 
de confusão organizada, de arbitrariedade consciente, de humanidade desumanizada, 
nada deve parecer natural nada deve parecer impossível de mudar.""")
