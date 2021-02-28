#Crie um programa onde o usuário possa digitar vários valores numéricos e 
# cadastre-os em uma lista.  Caso o número já exista lá dentro. Ele não seá adicionado 
#No final serão exibidos todos os valores únicos digitados em ordem crescente.
from os import system
system('cls')
lista = []
res = ''
while True:
    n = (int(input('Digite um valor: ')))
    if n not in lista:
        lista.append(n)
        print('Número adicionado a lista!')
    else:
        print('Numéro já existente não adcionado na lista')
    while True:
        res = str(input('Deseja continuar: [S/N]? ')).strip().upper()[0]
        if res  in 'SN':
            break
    if res == 'N':
        break
system('cls')
lista.sort()
print('Os Valores adicionados foram: ',end='')
for v in lista:
    print(f'{v} -> ',end='')
print(' FIM DO PROGRAMA!')
