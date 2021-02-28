import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do catedo adjacente: '))
hi = math.hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))