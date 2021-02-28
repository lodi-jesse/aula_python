# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal.
# Entre 25 e 30: Sobrepeso.
# Entre 30 e 40: Obesidade
# Acima de 40: Obesidade mórbida
import os
os.system('cls')
peso = int(input('Digite seu peso: '))
alt = float(input('Digite sua altura no formato ex.(1.50): '))
imc = peso / (alt * alt)
if imc < 18.5:
    print('Seu IMC é {:0.2f} e você esta abaixo do peso'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é {:0.2f} e você está no seu peso ideal'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é {:0.2f} e você está com sobrepeso'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é {:0.2f} e você está com obesidade'.format(imc))
elif (imc >= 40):
    print('Seu IMC é {:0.2f} e você está com obesidade mórbida'.format(imc))