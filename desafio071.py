import os
os.system('cls')
quat50 = quat20 = quat10 = quat1 = 0
print('='*35)
print('{:^35}'.format('BANCO BV'))
print('='*35)
valor = int(input('Que valor você quer sacar: R$\033[32m '))
if valor / 50 :
    quat50 = valor // 50 
    resto50 = valor - (quat50 * 50) 
if resto50 != 0:
    quat20 = resto50 // 20
    resto20 = resto50 - (quat20 * 20)
    if resto20 != 0:
        quat10 = resto20 // 10
        resto10 = resto20 - (quat10 * 10)
        if resto10 != 0:
            quat1 = resto10 // 1
print(f'\033[mTotal de {quat50} de R$ 50,00')
print(f'Total de {quat20} de R$ 20,00')
print(f'Total de {quat10} de R$ 10,00')
print(f'Total de {quat1} de R$ 1,00')
print('='*35)