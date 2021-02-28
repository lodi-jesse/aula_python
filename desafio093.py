lista_dec = {}
lista = []
soma = 0
lista_dec['nome']= str(input('Nome do jogador: '))
n = int(input('Quantas partidas ele jogou? '))
for i in range(0,n):
    lista.append(int(input(f'Quantos gols na {i +1}º partida: ')))
    lista_dec['gols']= lista[:]
for i in range(len(lista)):
    soma += lista[i]
lista_dec['total'] = soma
print('-='*30)
print(lista_dec)
print('-='*30)
for k,v in lista_dec.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {lista_dec["nome"]} jogou {n} partidas')
for i, j in enumerate(lista):
    print((f'=> Na partida {i + 1}, fez {j} gols'))
print(f'Foi um total de {lista_dec["total"]} gols')