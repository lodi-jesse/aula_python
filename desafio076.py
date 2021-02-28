from os import system
system('cls')
lista = ('Arroz', 4.5, 'Feijão', 6.30, 'Leite', 3, 'Café', 9.99, 'Açúcar', 7.9,'Óleo de cozinha', 15.9)
print(f'{"LISTA DE COMPRAS":^40}')
for i in range(0,len(lista)):
    if i % 2 == 0:
        print(f'{lista[i]:.<30}',end='')
    else:
        print(f'R${lista[i]:>7.2f}')