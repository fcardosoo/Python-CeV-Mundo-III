'''
Aprimore o ex093 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento
de cada jogador.
* Similar as funcionalidades do Boletim
* Se digitar nr de jogador que não existe informar erro e solicitar novamente
* 999 sai
'''

print('*'*50)
time = list()
jog = {}
nj = []

while True:
    jog.clear()
    jog['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Número de partidas {jog["nome"]} jogou? '))
    nj.clear()
    for c in range(0, tot):
        nj.append(int(input(f'     Quantos gols na partida {c+1}? ')))
    jog['gols'] = nj[:]
    jog['total'] = sum(nj)
    time.append(jog.copy())

    while True:
        resp = str(input('quer continuar? [S/N] ')).upper()[0] # [0] para pegar apenas o primeiro caracter
        if resp in 'SN':
            break
        print('ERRO! REsponda apenas S ou N.')
    if resp == 'N':
        break
print('-='*25)
print('cod', end='')
for i in jog.keys():
    print(f'{i:<20}', end='')
print()
print('=-='*17)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<20}', end='')
    print()

'''print('='*30)
print(jog)
print('='*30)
for c, d in jog.items():
    print(f'O campo {c} tem o valor: {d}')'''

print('='*50)

'''print(f'O jogador {jog["nome"]} jogou {jog["partidas"]} partidas.')
for i in range(0, jog['partidas']):
    print(f'=> Na partida {i+1}, fez {jog["gols"][i]} gols')
print(f'Em um total de {jog["total"]} gols.')
print('='*30)'''

while True:
    busca = int(input('Mostrar dados de qual jogador? [999 -> sai] '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe o jogador com o código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('<< VOLTE SEMPRE >>')
