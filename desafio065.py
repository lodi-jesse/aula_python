''' Crie um program que leia vários números inteiros pelo teclado, No final da execução mostre a média entre os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores  '''
media = cont = soma = maior = menor = 0
res = 'S'
while res in 'S':
    n = int(input('Digite um número: '))  
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    res = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
media = soma / cont
print('a média dos valores é {:.2f}'.format(media))
print('O maior número é {} e o menor número é {}'.format(maior,menor))
print('Fim!')
