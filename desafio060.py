''' faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 
5! = 5 X 4 X 3 X 2 X 1 = 120 '''
n = int(input('Digite um valor: '))
f = 1
print('O fatorial de {}! = '.format(n), end='')
while n > 0:
    print('{}'.format(n),end='')
    print(' X ' if n > 1  else ' = ', end='')
    f *= n
    n -= 1
print('{}'.format(f), end='')