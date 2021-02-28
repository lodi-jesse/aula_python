'''faça um programa que leia o sexo de uma pessoa.Mas só aceita valores [M]ou [f].
Caso esteja errado peça a digitação novamente até ter um valor correto.'''
import os
os.system('cls')
sexo = str(input('Informe seu sexo [M\F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dado invalido. Por favor informe seu sexo: ')).strip().upper()[0]
print('sexo {} registrado com sucesso'.format(sexo))