import os
os.system('cls')
cont = contm = contf20 = 0
res = ''
while True:
    print('='*30)
    print('CADASTRE UMA PESSOA')
    print('='*30)
    idade = int(input('Idade: '))
    while True:
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if sexo in 'MF':
            break
    print('='*30)
    while True:
        res = str(input('Deseja continuar [S/N]: ')).strip().upper()[0] 
        if res in 'SN':
            break
    if idade > 18:
        cont += 1
    if sexo == 'M':
        contm += 1
    if sexo == 'F' and idade < 20:
        contf20 += 1
    if res == 'N':
        break
print('='*5,'FIM DO PROGRAMA','='*5)
print(f'''Total de pessoas com mais de 18 anos: {cont}
Ao todo temos {contm} homens cadastrado.
E temos {contf20} mulheres com menos de 20 anos ''')
