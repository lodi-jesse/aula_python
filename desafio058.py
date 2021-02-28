'''Melhorar o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 á 10.
Só que agora o jogador vai tentar adivinhar a té acertar, mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint
from time import sleep
import os
sorteio = randint(0 ,10)
cont = 1
os.system('cls')
print('===== Tenta adivinhar o número que estou pensando de 0 até 10 =====')
n = int(input('Digite um número: '))
print('PROCESSANDO...')
sleep(1)
while sorteio != n:
    if sorteio < n:
        res = 'Menor'
    else:
        res = 'Maior'
    n = int(input('Você errou digite um número novamente {}: '.format(res)))
    print('PROCESSANDO...')
    sleep(1)
    cont += 1
print('Você acertou o número que eu estava pensando é {} e você digitou {}º vez parabéns!!!'.format(sorteio,cont))