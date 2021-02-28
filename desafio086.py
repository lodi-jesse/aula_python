'''crie um program que crie um matriz de dimensão 3x3 e preencha com valores
lidos pelo teclado
no final mostre a matriz na tela coma formaçao correta.'''
from os import system
system('cls')
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        matriz[i][j]=(int(input(f'Digite um valor {i,j}:')))
print('='*30)
for i in range (0,3):
    for j in range(0,3):
        print(f'[{matriz[i][j]:^5}]',end='')
    print()