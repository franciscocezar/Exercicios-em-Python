larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))

area = larg * alt

print(f'A parede tem a dimensão de {larg}x{alt} e sua área é de {area}m².')

tinta = area / 2

print(f'Para pintar essa parede, você precisará de {tinta}l de tinta.')
