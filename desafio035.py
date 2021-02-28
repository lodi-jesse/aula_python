# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou formar um triângulo.
r1 = int(input('Digite a primeira reta: '))
r2 = int(input('Digite a segunda reta: '))
r3 = int(input('Digite a terceira reta: '))
if (r1 + r2) > r3 and (r2 + r3) > r1 and (r3 + r1) > r2:
    print('As medidas {}, {} e {} formam um triângulo'.format(r1,r2,r3))
else:
    print('As medidas {}, {} e {} não formam um triângulo'.format(r1,r2,r3))