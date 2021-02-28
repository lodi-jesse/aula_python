''' Crie um programa que vai vários números e colocar em um lista
Depois disso, mostre:
A -> Quantos números forma digitados.
b -> A lista de valores ordenada de forma decrescente.
c -> Se o valor 5 foi digitado e está ou não na lista.'''
from os import system
system('cls')
lista = []
cont = 0
res = ''
while True:
    lista.append(int(input('Digite um valor: ')))
    cont += 1
    while True:
        res = str(input('Deseja continuar: [S/N]? ')).strip().upper()[0]
        if res in 'SN':
            break
    if res == 'N':
        break
print(f'A quantidade de números digitado foi {cont}')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print('O número 5 esta na lista.')
else: 
    print('O número 5 não está na lista.')

print('FIM DO PROGRAMA!')