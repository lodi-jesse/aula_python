print('<<<<<<<<<<<<<<<<<< Calcule o desconto do produto >>>>>>>>>>>>>>>')
valor = float(input('Digite o valor do produto: '))
desc = valor - (valor*5/100)
print('O valor do produto é de R${} com 5% de desconto o produto sai por R${:0.2f}'.format(valor,desc))