#Escreva um programa que faça o computador sortear um número de 0 ate 5 e pesa para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
sorteado = randint (0, 5) #faz o computador a sortear um número 
print('-=-' * 20)
num = int(input('Digite um número de "0 até 5" e tente a sorte: '))
print('-=-' * 20)
print('PROCESSANDO ...')
sleep(3)
if sorteado == num:
    print('O computador escolheu {} e você digitou {}. PARABÉNS VOCÊ VENCEU!'.format(sorteado,num))
else:
    print('O computador escolheu {} e você digitou {}. MAIS SORTE DA PROXIMA VOCÊ PERDEU!'.format(sorteado,num))
