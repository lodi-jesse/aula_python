import os
os.system('cls')
cont =  0
while True:
    print('-='*20)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-='*20)
    if n < 0:
        break
    for cont  in range(0,10):
        cont += 1
        print(f'{cont:2} X {n} = {cont*n}')
print('Programa tabuada encerrado. Volte sempre!')
