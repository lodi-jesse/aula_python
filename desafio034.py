# Escreva um programa que pergunte o salãrio de um funcionário e calcule o valor do seu aumento.
# Para salário superiores a R$1250,00 , calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
sal = float(input('Digite o salario: '))
if sal > 1250:
    nsal = (sal * 10 / 100) + sal
    print('O novo salário com o reajuste é de R${} reais'.format(nsal))
else:
    nsal = (sal * 15 / 100) + sal
    print('O novo salário com o reajuste é de R${} reais'.format(nsal))