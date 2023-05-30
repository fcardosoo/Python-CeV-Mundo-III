'''
Criar uma tupla (listagem) com produtos e preços
ao final printar uma tabela com produto e preço
Alinhados e formatados
'''

produtos = ('Lápis', 1.75,
            'Borracha', 2.0,
            'Caderno', 15.9,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-'*35)
print(f'{"LISTAGEM DE PREÇOS":^35}')
print('-'*35)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<25}', end = '')
    else:
        print(f'R${produtos[pos]:>7.2f}')
print('-'*35)
