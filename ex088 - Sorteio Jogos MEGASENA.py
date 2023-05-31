'''
Faça um programa que ajude um jogador da MEGASENA
a criar palpites. O programa vai perguntar
quantos jogos serão gerados e vai sortear 6 números
entre 1 e 60 para cada jogo, cadastrando tudo em um
lista composta
'''
import random
import time

print('~-'*10, 'GERADOR DE PALPITE', '~-'*10)

quant = int(input('Quantos jogos você deseja gerar? '))
jogos = []
palpites = []
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = random.randint(1, 60)
        if num not in jogos:
            jogos.append(num)
            cont += 1
        if cont >= 6:
            break
    jogos.sort()
    palpites.append(jogos[:])
    jogos.clear()
    tot += 1

print('-='*3, f'SORTEANDO {quant} JOGOS','-='*3)

for i, l in enumerate (palpites):
    print(f'Jogo {i+1}: {l}')
    time.sleep(1.3)
print('-='*5, '< BOA SORTE >', '-='*5)
