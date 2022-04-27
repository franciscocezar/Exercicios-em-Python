n = float(input('Digite um valor em metros: '))
cm = n * 100
mm = n * 1000
dm = n * 10
dam = n / 10
hm = n / 100
km = n / 1000

print(f'a media  de {n}m coresponde a: \n{km}km \n{hm}hm \n{dam}dam \n{dm:.0f}dm \n{cm:.0f}cm \n{mm:.0f}mm')