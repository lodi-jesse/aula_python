#A confederação nacional de natação precisa de um programa que que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade:
# até 9 anos : MIRIN
# até 14 anos : INFANTIL
# até 19 anos: JUNIOR
# até 24 anos: Senior
# Acima: MASTER
from datetime import date
print('<>'*5,'Federação de natação','<>'*5)
ano = int(input('Digite o ano de nascimento com 4 dígitos ex. 9999: '))
idade = date.today().year - ano 
if idade <= 9:
    print('Você tem {} anos e sua categoria é Mirin'.format(idade))
elif idade >= 10 and idade <= 14:
    print('Você tem {} anos e sua categoria é Infantil.'.format(idade))
elif idade >= 15 and idade <=19:
    print('Você tem {} anos e sua categoria é Junior.'.format(idade))
elif idade >=20 and idade <= 24:
    print('Você tem {} anos e sua categoria é Senior.'.format(idade))
else:
    print('Você tem {} anos e sua categoria é Master.'.format(idade))