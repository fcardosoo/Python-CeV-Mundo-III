# Ler o nome e o peso de várias pessoas, guardar tudo em uma lista
# a) Quantas pessoas foram cadastradas?
# b) Uma listagem com as mais pesadas
# c) Uma listagem com as mais leves

lista = []
temp = []
# cont = int()  # Se usar o contador precisa habilitar a criação desta variável

print('-'*30)
print('***** CADASTRAMENTO *****')
print('-'*30)

while True:
    temp.append(str(input('Qual o seu nome? ')))
    temp.append(float(input('Qual o seu peso? ')))

    if len(lista) == 0:
        men = mai = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]

    lista.append(temp[:])
    temp.clear()
    # cont += 1 # Contador de registros
    c = str(input('Deseja continuar [S/N]? '))
    if c in 'Nn':
        break
print('-='*30)
# lista.sort() # Para colocar a lista em ordem alfabética
print(f'Você cadastrou {len(lista)} pessoas.')
#print(f'Os dados digitados foram {lista}') #Este comando não foi solicitado
print(f'O maior peso foi de {mai}Kg. Peso de ', end = ' ')
for p in lista:
    if p[1] == mai:
        print(f'[{p[0]}]', end = ', ')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end = ' ')
for q in lista:
    if q[1] == men:
        print(f'[{q[0]}]', end = ', ')