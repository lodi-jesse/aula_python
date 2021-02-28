''' Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for. '''
s = 0 
n = int(input('Digite um número: '))
for c in range(1 , 10 + 1):
    s = c * n 
    print('{:2} X{:2} = {:2}'.format(c,n,s))
