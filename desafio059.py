''' Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa 

Seu programa deverá realizar a operação solicitada em cada caso. '''
import os
from time import sleep
os.system('cls')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
op = 0
while op != 5:
    print('''MENU
    [1] somar
    [2]multiplicar
    [3]maior
    [4]novo número
    [5]sair do programa''')
    op = int(input('>>>>>> Digite sua opção: '))
    if op == 1:
        soma = n1 + n2
        print('A somo entre {} e  {} é {}'.format(n1, n2, soma))
    elif op == 2:
        produto  = n1 * n2
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, produto))
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('entre {} e {} o maior valor é {}'.format(n1, n2,maior))
    elif op == 4:
        print('Informe os números novamente:')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif op == 5:
        print('finalizando...')
    else:
        print('Opção invalida tente novamente')
    print('=-=' * 10)
    sleep(5)
    os.system('cls')
print('fim do programa. Volte sempre! ')
    
    