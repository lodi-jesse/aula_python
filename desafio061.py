'''Refaça o DESAFIO 051 lendo o primeiro termo e a razão de uma PA.  Mostrando os 10 primeiros termos da progressão usando a estrutura while '''
import os
os.system('cls')
cont = 1
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
while cont <= 10:
    print('{} -> '.format(primeiro), end='')
    primeiro += razao
    cont += 1
print('fim')