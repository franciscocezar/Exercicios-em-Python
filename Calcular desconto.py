preco = float(input('Qual o preço do produto? R$'))
desc = preco - (preco * 5 / 100)

print(f'Preço do produto: R${preco:.2f} \nCom 5% de desconto, o valor final é R${desc:.2f}')

