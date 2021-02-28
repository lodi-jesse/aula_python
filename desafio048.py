''' Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 ate  500'''
s = 0
cont = 0
for c in range(1, 500 + 1, 2):
    if c % 3 == 0:
        cont += 1
        s += c
print('A soma de todos os {} valores solicitados é {}'.format(cont,s))
