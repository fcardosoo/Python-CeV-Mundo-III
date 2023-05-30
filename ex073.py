'''
Criar uma tupla com os 20 colocados do brasileirão
serie A por ordem de colocação.
a) Mostrar os primeiros 5
b) os últimos 5
c) ordem alfabética
d) em que posição esta a chapecoense?
'''

times = ('Sao Paulo', 'Internacional', 'Atletico-MG', 'Flamengo',\
        'Gremio', 'Palmeiras', 'Fluminense', 'Santos', 'Corintians',\
        'Athletico-PR', 'Ceará SC', 'Atletico-GO', 'Bragantino', \
        'Sport Recife', 'Fortaleza', 'Vasco da Gama', 'Bahia',\
        'Goiás', 'Botafogo', 'Coritiba')

print('~'*80)
print(f'Os primeiros 5 times no momento são: \n{times[:5]}')
print('~'*80)
print(f'Os últimos 5 colocados são: \n{times[15:]}')
print('~'*80)
print(sorted(times))
print('~'*80)
posicao = str(input('Qual time você quer consultar? '))
print(f'O {posicao} está na {times.index(posicao)+1}ª posição neste momento.')
print('~'*80)