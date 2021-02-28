''' Melhor o DESAFIO 061 perguntando para o usuário se ele quer mostra mais alguns termos. 
O programa encerra quando ele disse que quer mostra [0] termos '''
import os
os.system('cls')
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo =  primeiro
mais = 10
cont = 1
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('digite quantos termos quer a mais: '))      
print('Programa finalizador com {} termos mostrado'.format(total))
