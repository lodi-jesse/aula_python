print('<<<<<<<<<<<<<<<< CONVERSOR DE METRO PARA CM E MM >>>>>>>>>>>>>>>>')
mt = float(input('Digite um número: '))
dm = mt * 10
cm = mt * 100
mm = mt * 1000
dam = mt * 0.10
hm = mt * 0.01
km = mt * 0.001
print('{} km \n{} hm \n{} dam \n{} mt \n{} dm \n{} cm \n{} mm'.format(km,hm,dam,mt,dm,cm,mm))