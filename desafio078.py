#Faça um programa que leia 5 valore numéricos e guarda os em um lista.
# No final mostre qual foi o maior e o menor valor digitado e os suas respetivas 
# posições na lista
from random import randint
from os import system
system('cls')
lista = []
maior = menor = 0
for c in range(0,5):
    lista.append(randint(0,10))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(lista)
print(f'O maior valor digitado foi {maior} na posição ', end ='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{v}...',end='')
print()
print(f'O menor valor digitado foi {menor} ma posição ',end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...',end='')