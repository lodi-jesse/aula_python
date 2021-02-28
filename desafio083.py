''' Crie um programa onde o usuário digita um expressão qualquer que use 
parênteses. Seu aplicarivo deverá analisar se a expressão passada está com os 
parênteses na ordem correta. '''
from os import system
system('cls')
exp = str(input('Digite a expressão: '))
pilha = []
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
        break
if len(pilha) == 0:
    print('Sua expressão está certa')
else:
    print('Sua expressão está errada.')