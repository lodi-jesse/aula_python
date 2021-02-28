'''Faça um programa que ajude um jogador da mega sena a criar palpites 
o programa vai perguntar quantos jogos serão gerando e vai sortear 6 números entre 1 e 60
para cada jogo,  cadastrado tudo em uma lista composta'''
from os import system
from random import randint
from time import sleep
system('cls')
lista = []
jogo = []
def espaco():
    print('='*30)
quant = int(input('Quantos jogos deseja criar:\033[32m '))
print('\033[m')
espaco()
print('{:^40}'.format('\033[36mMEGA CENA\033[m'))
espaco()
for c in range(0,quant):
    for i in range (0,6):
        n = randint(1,60)
        jogo.append(n)
        jogo.sort()
        sleep(0.5)
    print(f'O jogo \033[32m{(c)+1}\033[mº foi criado com estes número: \033[32m{jogo}\033[m')
    espaco()
    lista.append(jogo[:])
    jogo.clear()
    c += 1
print('BOA SORTE! Volte sempre.')
