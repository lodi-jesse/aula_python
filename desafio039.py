#Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
#Se ele ainda vai se alistar são serviço militar.
#Se é a hora de se alistar.
#Se jpa passou do tempo do alistamento.
#Seu program também deverá mostra o tempo que falta ou que passou do prazo.
from datetime import date
ano = int(input('Digite o ano de seu nascimento com 4 dígitos ex. 9999: '))
idade = date.today().year - ano
if idade == 18:
    print('Você tem {} anos e deverá se alistar no serviço militar este ano.'.format(idade))
elif idade < 18:
    falta = (18 - idade)
    print('Você tem {} anos e falta {} anos para se alistar no serviço militar.'.format(idade,falta))
else:
    passou = (idade - 18)
    print('Você tem {} anos e passou {} anos para se alistar no serviço militar'.format(idade,passou))