from random import randint
jogador = {}
lista = []
mai = men = 0
for i in range(0,4): 
    jogador['nome'] = (f'jogador{i +1 }')
    jogador['acerto'] = randint(1,6)
    lista.append(jogador.copy())
for i in lista:
    print(f"O {i['nome']} tirou {i['acerto']}")
for i in lista:
    if i == 0:
        mai = men = jogador['acerto':]
    else:
        if jogador['acerto'] > mai:
            mai = jogador['acerto']
        if jogador['acerto'] < men:
            men = jogador['acerto']
print(mai)
print(men)