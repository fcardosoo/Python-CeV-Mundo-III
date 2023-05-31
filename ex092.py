'''
Criar um programa que leia: nome, ano de nascimento e CTPS
e cadastre-os (com idade) em um dicionário se por acaso a CTPS
for diferente de zero, o dicionário receberá também o ano de
contratação e o salário. Calcule e acrescente, além da idade,
com quantos anos a pessoa vai se aposentar.
* Aposentar = 35 anos de contribuição.
* Usar um laço para ler o dicionário.
'''
from datetime import datetime

print('-='*20)

funcionario = {}
funcionario['nome'] = str(input('Nome: '))

anas = int(input('Ano de Nascimento: '))
funcionario['idade'] = datetime.now().year - anas
funcionario['CTPS'] = int(input('CTPS: '))
if funcionario['CTPS'] != 0:
    funcionario['contratação'] = int(input('Ano de contratação: '))
    funcionario['Salário'] = float(input('Salário: R$'))
    funcionario['Aposentadoria'] = funcionario['idade'] + ((funcionario['contratação'] + 35) - datetime.now().year)

print('-='*30)
for k, v in funcionario.items():
    print(f' - {k} tem o valor {v}')