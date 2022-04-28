from math import radians, sin, cos, tan

angulo = float(input('Digite o valor do ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'O ângulo de {angulo:.0f}º tem: \nSENO de {seno:.2f} \nCOSSENO de {cosseno:.2f} \nTANGENTE de {tangente:.2f}')
