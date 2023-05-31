'''
Ler o NOME, SEXO e IDADE de várias pessoas, guardando os
dados de cada pessoa em um DICIONÁRIO e todos os dicionários
em uma LISTA. No final mostre:
a) Quantas pessoas foram cadastradas
b) A média de idade do grupo
c) Uma lista com todas as mulheres
d) Uma lista com todas as pessoas com idade acima da média.
'''

pessoa = dict() #criando um dicionario
galera = list()
soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor digite M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    galera.append(pessoa.copy())
    soma += pessoa['idade']
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('*-'*30)

# quantas pessoas foram cadastradas?
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')

# qual a média das idades
media = soma/len(galera)
print(f'B) A média das idades é {media:5.2f} anos')

# quantas mulheres cadastradas?
print(f'C) As mulheres cadastradas foram ', end=' ')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')
print()
# Pessoas que tem idade acima da média
print(f'A lista de pessoas que estão acima da média: ', end=' ')
for p in galera:
    if p['idade']>= media:
        print(f'{p["nome"]}', end=' ')