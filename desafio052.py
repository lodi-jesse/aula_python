''' faça um programa que leia um número inteiro e diga se ele é ou não um número primo. '''
tot =0
n = int(input('Digite um número: '))
for i in range(1, n +1):
    if n % i == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end= ' ')
    print('{}'.format(i), end=' ')
print()
print('\033[mO número {} foi divisível {} vezes'.format(n, tot))
if tot == 2:
    print('E por isso ele é primo')
else:
    print('E por isso ele não é primo')
