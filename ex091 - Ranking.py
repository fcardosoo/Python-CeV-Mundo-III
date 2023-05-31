'''
Criar um programa onde 4 jogadores joguem um dado e tenham
resultados aleatórios. Guarde esses resultados em um dicionário.
No final, coloque este dicionário em ordem, sabendo que o vencedor
tirou o maior número no dado.
'''

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}
ranking = ()
print('::: Valores sorteados :::')
sleep(1)
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# Usado a função itemgetter para ordenar o dicionário usar parte 1, se usar parte ZERO (0) ordena as chaves
# Usar o reverse=True para colocar em ordem decrescente
sleep(1)
print('-='*30)
sleep(1)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(.8)
print('Finalizando...')
sleep(1)
print('-='*30)