'''
Crie uma matriz de dimensão 3x3 e preencha com
valores lidos pelo teclado. No final mostre com a formatação
correta.
'''

matriz = [[], [], []]

for c in range(1, 4):
    matriz[0].append(int(input(f'Digite um valor para [0, {c}]: ')))
for c in range(1, 4):
    matriz[1].append(int(input(f'Digite um valor para [1, {c}]: ')))
for c in range(1, 4):
    matriz[2].append(int(input(f'Digite um valor para [2, {c}]: ')))
print('*-'*15)
print(f'{matriz[0]}\n'
      f'{matriz[1]}\n'
      f'{matriz[2]}')

''' GUANABARA

matriz = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]

for l in range(0, 3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
    
    print('*-'*30)
for l in range(0, 3):
    for c in range (0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

'''