'''
Leia nome e 2 notas de vários alunos
mostrar boletim com a média de cada um
e permitir que seja exibida as notas de cada aluno individualmente
'''

alunos = []
temp = []

cont = 'S'
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    temp.append(nome)
    temp.append(n1)
    temp.append(n2)
    alunos.append(temp[:])
    temp.clear()
    cont = input('Deseja continuar [S/N]'.upper())
    if cont in 'Nn':
        print('FINALIZANDO...')
        break
print('-='*20)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)
for i, l in enumerate(alunos):
    print(f'{i:<4}{alunos[i][0]:<10}{(alunos[i][1]+alunos[i][2])/2:>8.2f}')
print('-'*30)
c = 0
while c != 999:
    c = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if c != 999:
        print(f'Notas de {alunos[c][0]} são ', f'{alunos[c][1]} e ', f'{alunos[c][2]}')
        print('<<< Obrigado, volte sempre!!! >>>')
        print('-' * 30)