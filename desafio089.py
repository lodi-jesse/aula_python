'''Crie um program que leia nome e duas notas de vários alunos e guarde tudo em uma 
lista composta.  No final mostre um boletin comtendo a média de cada um e permita
que o usuário possa mostrar as notas de cada aluno individualmente.'''
from os import system
system('cls')
def espaco():
    print('='*30)
lista = []
print('{:^25}'.format('Dados dos alunos'))
espaco()
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    lista.append([nome,[n1,n2],media])
    while True:
        res = str(input('Deseja continuar:[S/N]? ')).strip().upper()[0]
        if res in 'SN':
            break
        print('\033[31mOpção invalida tente novamente!\033[m')
    if res == 'N':
        break
    system('cls')
system('cls')
print('{:^25}'.format('Boletin'))
espaco()
print(f'{"No.":<4}{"NOME":<10}{"Média":>8}')
espaco()
for i , a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True: 
    no = int(input('Mostrar a nota de qual aluno? (999 interrompe): '))
    if no == 999:
        break
    if no <= len(lista) -1:
        print(f'Notas de {lista[no][0]} são {lista[no][1]}')
print('<<<<< Volte sempre >>>>>')