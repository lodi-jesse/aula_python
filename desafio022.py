nome = str(input('Digite seu nome completo: ')).strip()
print('Analizador de nome ....')
print(nome)
print('='*30)
print('Seu nome em letras maiúsculo é {}'.format(nome.upper()))
print('='*30)
print('Seu nome em letras minúsculas é {}'.format(nome.lower()))
print('='*30)
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('='*30)
dividir = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(dividir[0], len(dividir[0])))