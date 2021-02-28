# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0,50 por km para viagems de até 200km e R$0,45 para viagens mais longas.
print('  CALCULE O PREÇO DA SUA VIAGEM  ')
print('='*35)
dist = int(input('Digite a distância da viagem em Km: '))
if dist <= 200:
    valor = dist * 0.50
else:
    valor = dist * 0.45
print('A distância da viagem é de {}Km e você vai pagar R${} reais'.format(dist,valor))