# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
print('Descubra se o número é par ou ímpar')
print('='*35)
num = int(input('Digite um número: '))
if num % 2 == 0:
    print('Você digitou o número {} e ele é Par'.format(num))
else:
    print('Você digitou o número {} e ele é Ímpar'.format(num))