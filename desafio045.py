# Crie um programa que faça o computador jogar JOKEMPÔ com você (pedra,  papel, tesoura)
import random
import os
os.system('cls')
from random import randint
from time import sleep
lista = ['Pedra','Papel', 'Tesoura']
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO !!!')
sleep(1)
print('-='*11)
print('Computador jogou {}'.format(lista[computador]))
print('Jogador jogou {}'.format(lista[jogador]))
print('-='*11)
if computador == 0:
        if jogador == 0:
                print('EMPATE')
        elif jogador == 1:
                print('JOGADOR VENCEU')
        elif jogador == 2:
                print('O COMPUTADOR VENCEU')
        else:
                print('JOGADA INVÁLIDA!')
elif computador == 1:
        if jogador == 0:
                print('O JOGADOR VENCEU')
        elif jogador == 1:
                print('EMPATE')
        elif jogador == 2:
                print('O COMPUTADOR VENCEU')
        else:
                print('JOGADA INVÁLIDA!')
elif computador == 2:
        if jogador == 0:
                print('O JOGADOR VENCEU')
        elif jogador == 1:
                print('O COMPUTADOR VENCEU')
        elif jogador == 2:
                print('EMPATE')       
        else:
                print('JOGADA INVÁLIDA!')
