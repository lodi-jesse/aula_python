# Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR.
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
#verificando o número maior.
if n1 > n2 and n1 > n3:
    print('O maior número é {}'.format(n1))
elif n2 > n1 and n2 > n3:
    print('O maior número é {}'.format(n2))
elif n3 > n1 and n3 > n2:
    print('O maior número é {}'.format(n3))
#verificando o número menor.
if n1 < n2 and n1 < n3:
    print('O menor número é {}'.format(n1))
elif n2 < n1 and n2 < n3:
    print('O menor número é {}'.format(n2))
elif n3 < n2 and n3 < n1:
    print('O menor número é {}'.format(n3))
