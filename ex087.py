'''
Aprimorar o desafio 86,
a) A soma de todos os valores pares digitados
b) A soma dos valores da terceira coluna
c) O maior valor da segunda linha
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('*-' * 18)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('~-' * 18)
print(f'A soma dos valores pares corresponde a: {spar}')

for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é: {scol}')
for c in range(0, 3):
    if matriz[1][c] > mai:
        mai = matriz[2][c]
print(f'O maior valor da segunda linha: {mai}')