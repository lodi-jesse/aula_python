''' Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostra:
-> A média de idade do grupo 
-> Qual é o nome do homem mais velho 
-> Quantas mulheres têm menos de 20 anos'''
somaidade = 0
mediaidade = 0
maioridadehomem = 0
totmulher20 = 0
nomevelho = ''
for i in range(1,5):
    print('====== {}º PESSOA ====='.format(i))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade
    if i == 1 and sexo in 'Mn':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem,nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))