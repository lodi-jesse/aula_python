# Faça um programa que leia um ano qualquer e mostra se ele é BISSEXTO.
from datetime import date #Puxar a data atual independente o sistema ou aprelho utilizado 
print('DESCUBRA SE O ANO É BISSEXTO')
print('='*30)
ano = int(input('Digite o ano exemplo."XXXX" ou digite "0" para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 == 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))