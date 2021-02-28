''' Crie uma programa que vai ler vários números e colocar em um lista.
Depois disso, crie duas listas extras  que vão conter apenas os valores pares 
e os valores impares digitados, respetivamente
Ao final, mostre o conteúdo das três listas geradas. '''
from os import system
system('cls')
lista =  []
listapar = []
listaimpar = []
res = ''
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
    while True:
        res = str(input('Deseja continuar: [S/N]? ')).strip().upper()[0]
        if res in 'NS':
            break
    if res =='N':
        break
print('='*25)
print(lista)
print('='*25)
print(listapar)
print('='*25)
print(listaimpar)
print('='*25)
print('FIM DO PROGRAMA! ')