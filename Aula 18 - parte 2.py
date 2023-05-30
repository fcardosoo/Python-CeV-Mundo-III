# LISTAS - Variáveis Compostas

dados = list()  # criando uma lista
dados.append('Pedro')  # inserindo um valor na posição Zero.
dados.append(25)  # inserindo o valor 25 na posição 1.
print(dados[0])  # imprimindo na tela 'Pedro'

pessoas = list()  # criando a lista 'pessoas';

pessoas.append(dados[:])  # copiando toda a lista dados p/ dentro de pessoas;
print(pessoas)
pessoas = ['Pedro', 25], ['Maria', 19], ['João', 32]
print(pessoas)

print(pessoas[0][0])  # Print o elemento 0 do item 0 = Pedro
print(pessoas[1])

for p in pessoas:  # para cada p (pessoa) em pessoas
    print(f'{p[0]} tem {p[1]} anos')  # imprima pessoa

# solicitar dados e guardá-los em uma lista
print('~~' * 10)
turma = []
dado = []
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    turma.append(dado[:])
    dado.clear()
print(turma)
print('=-' * 10)

# Imprimir apenas os maiores de idade

totmai = totmen = 0
for p in turma:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores.')
