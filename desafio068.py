import os
from random import randint 
os.system('cls')
res = ''
fim = ''
cont = 0
cup = randint(0,10)
print('=-'*13)
print('\033[36mVAMOS JOGAR PAR OU ÍMPAR\033[m')
print('=-'*13)
while True:
    n = int(input('Digite um valor:\033[32m '))
    res = str(input('\033[mPar ou Ímpar?[P/I]:\033[32m  ')).strip().upper()[0]
    print('\033[m='*26)
    soma = cup + n
    if res == 'I':
        if soma % 2 == 1:
            print(f'Você jogou {n} e o computador {cup}. Total {soma} e deu ímpar ')
            print('='*26)
            fim = 'VENCEU'
            cont += 1
            print(f'Você {fim}!')
        elif soma % 2 == 0:
            print(f'Você jogou {n} e o computador {cup}. Total {soma} e deu Par ')
            print('='*26)
            fim = 'PERDEU'
            print(f'Você {fim}!')  
    if res == 'P': 
        if soma % 2 == 0:
            print(f'Você jogou {n} e o computador {cup}. Total {soma} e deu Par')
            print('='*26)
            fim = 'VENCEU'
            cont += 1
            print(f'Você {fim}!')
        elif soma % 2 == 1:
            print(f'Você jogou {n} e o computador {cup}. Total {soma} e deu Ímpar')
            print('='* 26)
            fim = 'PERDEU'
            print(f'Você {fim}!')
    if fim == 'PERDEU':
        break
print(f'Game Over! Você venceu {cont}')