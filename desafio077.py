lista = ('aprender','programar','linguagem','python','curso','gratis','estudar','praticar','trabalhar'
,'mercado','programador','futuro')
for palavra in lista:
    print(f'\nA palavra {palavra.upper()} temos ... ',end= '')
    for letra in palavra:
       if letra.lower() in 'aeiou':
           print(letra , end='')