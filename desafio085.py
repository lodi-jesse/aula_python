'''Crie um program onde o usuário possa digitar 7 valores numéricos e
cadastre-os em uma lista única que mantenha separados os valores pares e 
ímpares. No final mostre os n=valores pares e impares em ordem crescente.'''
from os import system
system('cls')
lista = [[],[]]
for cont in range(0,7):
    n = int(input(f'Digite o {(cont)+1}º valor: '))
    if n % 2 == 0:
        lista[0].append(n) 
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print('='*30)
print(f'Os números pares digitados foi :{lista[0]}')
print(f'Os números ímpares digitados foi: {lista[1]}')