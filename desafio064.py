''' Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final mostre quantos números froram digitados e qual foi a soma entre eles.
Desconsiderando o flag número de saída  '''
cont = 0
soma = 0 
n = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        soma += n
    cont += 1
print('A quantidade de números digitados foi {} e a soma entre ele foi {}'.format(cont,soma))
print('Fim!')