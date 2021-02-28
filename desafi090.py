turma = dict()
turma['nome'] = str(input('Nome: '))
turma['media']= float(input(f'Média de {turma["nome"]}: '))
print(f'Nome é igual a {turma["nome"]}')
print(f'Média é igual a {turma["media"]}')
if turma['media'] >= 7:
    print('Situação é igual a Aprovado')
else:
    print('Situação é igual a Reprovado')