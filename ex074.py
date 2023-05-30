'''
Gerar 5 números aleatórios e colocar em uma tupla
mostar a listagem dos números;
mostrar o menor e o maior
'''

from random import randint

n = (randint(1, 10)), (randint(1, 10)), (randint(1, 10)),\
    (randint(1, 10)), (randint(1, 10))

print('~'*40)
print(f'Eu sortei os valores: {n}')
print('-'*40)
print(f'O maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')
print('~'*40)