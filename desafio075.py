from os import system
system('cls')
n = ((int(input('Digite o primeiro número:\033[32m '))),
(int(input('\033[mDigite o segundo número:\033[32m '))),
(int(input('\033[mDigite o terceiro número:\033[32m '))),
(int(input('\033[mDigite o quarto número:\033[32m '))))
print(f'\033[mO valor 9 aparece \033[32m{n.count(9)}\033[m vez(es)')
if 3 in n:
    print(f'O número 3 aparece na posição \033[32m{n.index(3)+1}\033[mº')
else:
    print('\033[31mO número três não foi digitado.\033[m')
print('Os números pares digitados foi: ',end='')
for par in n:
    if par % 2 == 0:
        print('\033[32m',par,'\033[m', end='')