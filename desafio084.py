'''Faça um program que leia nome e peso da varias pessoas
guardando tudo em uma lista. no final mostre
-> quantas pessoas foram cadastradas.
-> uma listagem com as pessoas mais pesadas.
-> uma listagem com as pessoas mais leves'''
from os import system
system('cls')
lista = []
dados = []
listapesado = []
listaleve = []
menor = maior = c = 0
while True:
        c += 1
        dados.append(str(input(f'Digite o {(c)}º nome: ')))
        dados.append(float(input(f'Digite o {(c)}º peso: ')))
        if len(lista) == 0:
            menor = maior = dados[1]
        else:
            if dados[1] > maior:
                maior = dados[1]
            if dados[1] < menor:
                menor = dados[1]
        lista.append(dados[:])
        dados.clear()
        while True:
            res = str(input('Deseja continuar: [S/N]? ')).strip().upper()[0]
            if res in 'SN':
                break
        if res == 'N':
            break
print('='*30)
print(f'A quantidade de pessoas cadastrada foi de {len(lista)}')
print(f'O maior peso digitado foi {maior}Kg e as pessoas que tem esse peso são: ',end='')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}, ',end='')
print()
print(f'O menor peso digitado foi {menor}kg e as pessoas que tem esse peso são: ', end='')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}, ',end='')


