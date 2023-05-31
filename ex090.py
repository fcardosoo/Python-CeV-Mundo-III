'''
Ler o NOME e MÉDIA de um aluno, guardando também a
situação em um DICIONÁRIO. Ao final mostrar o nome, a média
e a situação do aluno... >7 = Aprovado
'''

print('-='*15)
print(f'*'*10,'BOLETIM','*'*10)
print('-='*15)

aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'A média de {aluno["nome"]}: '))
print(f'- O nome do aluno é {aluno["nome"]}')
print(f'- A Média do aluno é {aluno["media"]}')
if aluno['media'] >= 7:
    print('- Situação é igual a APROVADO!')
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] >= 5:
    print('- Situação é igual a RECUPERAÇÃO!')
    aluno['situacao'] = 'Recuperação'
else:
    print('- Situação é igual a REPROVADO!')
    aluno['Situacao'] = 'Reprovado'
print('*-'*15)
print(aluno)