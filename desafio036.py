#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o "valor da casa", "o salário" do comprador e em "quantos anos" ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode excder "30%" do salário ou então o emprestimo será negado. 
print('=x='*5,'\033[1;32mFinanciamento de casa\033[m','=x='*5)
valor_casa = float(input('Digite o valor do imovél: '))
sal = float(input('Digite o salário: '))
tempo = int(input('Quantos anos gostaria de pagar o imóvel? '))
prestacao = valor_casa / (tempo * 12) 
if (sal*30/100) < prestacao:
    print('\033[4;31mSeu financiamento não foi aprovado!\033[m')
else:
    print('\033[4;36mParabéns seu financiamento foi aprovado com sucesso!\033[m')