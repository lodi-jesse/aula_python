import os
os.system('cls')
soma = cont = menor =  0
maisbarato = res = ''
print('=-'*20)
print('{:^40} '.format('LOJA SUPER BARATÃO'))
print('=-'*20)
while True:
    produto = str(input('\033[mNome do Produto:\033[32m ')).strip()
    preco = float(input('\033[mPreço: R$\033[32m '))
    while True:
        res = str(input('\033[mQuer continuar: [S/N]\033[32m ')).strip().upper()[0]
        if res in 'SN':
            break   
    soma += preco
    if preco > 1000:
        cont += 1
    if cont == 1 or preco < menor:
        maisbarato = produto
        menor = preco
    if res == 'N':
        break
print('{:^40}'.format('\033[mFIM DO PROGRAMA','='*5))
print(f'''O total de compra foi R${soma}
Temos {cont} produtos que custam mais de R$1000,00
O produto mais barato foi {maisbarato} que custou R${menor}''')