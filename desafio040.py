#Faça um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final. de acordo com a média atingida:
# Média abaixo de 5.0: reprovado 
# Média ente 5.0 e 6.9: Recuperação
# Média 7.0 ou superior: Aprovado
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
mdia = (n1 + n2) / 2 
if mdia < 5.0:
    print('você tirou uma média de \033[31m{:0.2f}\033[m e está \033[4;31mREPROVADO\033[m.'.format(mdia))
elif mdia > 5.0 and mdia < 6.9:
    print('Você tirou uma média de \033[33m{:0.2f}\033[m e está de \033[4;33mRECUPERAÇÃO\033[m.'.format(mdia))
elif mdia >= 7.0:
    print('Você tirou uma média de \033[36m{:0.2f}\033[m e foi \033[4;36mAPROVADO\033[m.'.format(mdia))