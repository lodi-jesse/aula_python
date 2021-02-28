from datetime import date
ano_atual = date.today().year
lista_dic = {}
lista_dic['nome']=str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
lista_dic['idade'] = ano_atual - ano
ctps = int(input('Carteira de trabalho (0 não tem): '))
if ctps != 0:
    lista_dic['ctps'] = ctps
    lista_dic['contratação'] =  int(input('Ano de contratação: '))
    lista_dic['salario'] = float(input('Salário: R$ '))
    anotr = ano_atual - lista_dic['contratação']
    lista_dic['aposentadoria'] = (35 - anotr) + lista_dic['idade']
    print('-='*30)
    for k, v in lista_dic.items():
        print(f'{k} tem o valor {v}')
print('-='*30)
for k, v in lista_dic.items():
    print(f'{k} tem o valor {v}')