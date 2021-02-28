dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km foi rodado? '))
pago = (dias * 60) + (km * 0.15)
print('O total a ser pago é de R${:0.2f}'.format(pago))