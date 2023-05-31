'''Digitar 5 valores cadastra-los em
uma lista já na posição correta de inserção
sem o uso do SORT
Exibir a lista ordenada'''

lista = []

for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na possição {pos} da lista...')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')