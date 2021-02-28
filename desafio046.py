'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,  indo de 10 até 0 e com uma pausa de 1 segundo entre eles'''
import os
from time import sleep
os.system('cls')
print('-=='*5,'\033[32mCONTAGEM REGRESSIVA\033[m','==-'*5)
for c in range(10 , -1, -1):
    sleep(1)
    print('\033[33;40m',c,'\033[m')
os.system('cls')
sleep(0.5)
print('\033[35mFeliz ano novo!!!!\033[m')