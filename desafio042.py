# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: Todos os lados diferentes 
r1 = int(input('Digite a primeira reta: '))
r2 = int(input('Digite a segunda reta: '))
r3 = int(input('Digite a terceira reta: '))
if (r1 + r2) > r3 and (r2 + r3) > r1 and (r1 + r3) > r2:
    input('Sim estas retas formam um triângulo')
    if r1 == r2 == r3:
        print('Ete triângulo é um Equilátero.')
    elif r1 != r2 != r3 != r1:
        print('Este triângulo é um isósceles.')
    else:
        print('Este triângulo é escaleno')
else:
    print('Essas retas não formam um triângulo.')