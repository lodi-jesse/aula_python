''' Desenvolva um porgrama que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se for ímpar desconsidere-o '''
s = 0 
cont = 0
for c in range(1, 7):
    n = int(input('Digite un {}º número inteiro: '.format(c)))
    if n % 2 == 0:
        s += n
        cont += 1
print('A soma entre os {} números pares digitados foi {}'.format(cont,s))