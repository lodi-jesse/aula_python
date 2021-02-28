# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu peço normal e condição de pagamento:
# Á vista dinheiro\ cheque: 10% de desconto 
#Á vista no cartão: 5% de desconto 
# Em 2x no cartão: preço normal 
# 3X ou mais no cartão 20% de juros
import os
os.system('cls')
preco = float(input('Digite o valor do produto: '))
print('-=-'*5,'FORMA DE PAGAMENTO','-=-'*5)
print('[1] À vista dinheiro/ cheque')
print('[2] À vista no cartão')
print('[3] Em 2X no cartão')
print('[4] Em 3X ou mais no cartão')
forma = int(input('Escolha a forma de pagamento: '))
if (forma == 1):
    valor = preco - (preco * 10 / 100)
    print('O valor do Produto a ser pago é R$ {:.2f} reais'.format(valor))
elif(forma == 2):
    valor = preco - (preco * 5 / 100)
    print('O valor do produto a ser pago é R$ {:.2f} reais'.format(valor))
elif(forma == 3):
    valor = preco / 2 
    print('O valor a ser pago pelo produto é R$ {:.2f} e será pago em duas vezes de R$ {:.2f} reais'.format(preco,valor))
elif(forma == 4):
    valor = preco + (preco * 20 / 100)
    print('O valor a ser pago será de R$ {:.2f} reais e pode ser parcelado em até 10X'.format(valor))


























3