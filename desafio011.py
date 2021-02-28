print(' <<<<<<<<<<<<< Quanto você vai gastar de tinta >>>>>>>>>>>>>>> ')
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
litro = area / 2
print('Sua parede tem a dimensão de {} X {} e sua área é de {}'.format(largura,altura,area))
print('Você precisa para pintar a parede de {} litros de tinta'.format(litro))