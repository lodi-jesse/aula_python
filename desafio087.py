'''Aprimore o desafio 86 mostrando no final 
-> a soma de todos os valore pares digitados
-> a soma do valores da terceira coluna
-> P maior valor da segunda linha f'''
from os import system
from random import randint
system('cls')
matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma = soma3 = 0
for i in range(0,3):
    for j in range(0,3):
        matriz[i][j]= randint(0,100)
        if matriz[i][j] % 2 == 0:
            soma += matriz[i][j]
for i in range(0,3):
    soma3 += matriz[i][2]
for j in range(0,3):
    if j == 0:
        maior = matriz[1][j]
    elif matriz[1][j] > maior:
        maior = matriz[1][j]
for i in range(0,3):
    for j in range(0,3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()
print(f'A soma de toda a matriz é {soma}')
print(f'A soma da terceira coluna é {soma3}')
print(f'O maior valor da segunda linha é {maior}')