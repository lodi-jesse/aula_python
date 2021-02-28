''' Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.(considerar maior idade 21) '''
from datetime import date
ano_atual = date.today().year
menor = 0
maior = 0
for c in range(1, 7 +1):
    ano = int(input('Digite o ano que a {}º pessoa nasceu com 4 dígitos Ex.9999: '.format(c)))
    idade = ano_atual - ano
    if idade < 21:
        menor += 1 
    else: 
        maior += 1
print('''A pessoas que ainda não atigiram a maior idade é {}.
As pessoas que já passaram da maior idade é {}'''.format(menor,maior))