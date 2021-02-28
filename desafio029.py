# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/p, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada km acima do limite.
velo = int(input('Lendo a velocidade do carro: '))
if velo > 80:
    multa = ( velo - 80 ) * 7
    print('Você passou a {}km/p e foi multado em R${} reais'.format(velo,multa))
else:
    print('Tenha um bom dia e continue dirigindo com cuidado!')