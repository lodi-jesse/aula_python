import os
os.system('cls')
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito','dezanove', 'vinte')
while True:
    while True:
        n = int(input('digite um número entre 0 e 20:\033[32m '))
        print('\033[m',end='')
        if  0 <= n <= 20:
            break
    print(f'Você digitou o número {cont[n]}')
    while True:
        res = str(input('Deseja continuar: [S/N]? ')).strip().upper()[0]
        if res in 'SN':
            break
    if res == 'N':
        break
print('fim do programa!')