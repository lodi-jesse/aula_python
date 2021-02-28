'''Escreva um programa que leia um número [n] inteiro qualquer e mostre na tela os [n] primeiros elementos de uma SEQUENCIA DE FIBONACCI'''
t1 = 0
t2 = 1
cont = 2
n = int(input('Digite a quantidade de fibonacci: '))
print('{} -> {} -> '.format(t1,t2),end='')
while cont < n :
    t3 = t1 + t2
    print('{} -> '.format(t3),end='')
    t1 = t2 
    t2 = t3
    cont += 1
print('Fim!')