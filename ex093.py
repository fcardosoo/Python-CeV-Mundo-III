"""
Crie um programa que gerencie o aproveitamento de um jogador de
futebol. O programa vai ler o nome do jogador e quantas partidas ele
jogou. Depois vai ler a quantidade de gols feitos em cada partida
(em uma lista). No final, tudo será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.
Campos: nome, gols, total"""

print('*'*50)
jog = {}
nj = []
jog['nome'] = str(input('Nome do jogador: '))
jog['partidas'] = int(input('Número de partidas: '))
for i in range(0, jog['partidas']):
    n = int(input(f'Quantos gols na partida {i+1}: '))
    nj.append(n)
jog['gols'] = nj[:]
jog['total'] = sum(nj)

print('='*30)
print(jog)
print('='*30)

for c, d in jog.items():
    print(f'O campo {c} tem o valor: {d}')
print('='*30)

print(f'O jogador {jog["nome"]} jogou {jog["partidas"]} partidas.')
for i in range(0, jog['partidas']):
    print(f'=> Na partida {i+1}, fez {jog["gols"][i]} gols')
print(f'Em um total de {jog["total"]} gols.')
print('='*30)
