''' Digitar 7 valores numericos em uma única lista,
que mantenha separados os pares e os ímpares, no final
mostre os pares e os impares em ordem crescente'''

temp = []
lista = [[], []]

for c in range (0, 7):
    c = int(input(f'Digite o {c+1}º valor: '))
    temp.append(c)
for d in temp:
    if d % 2 == 0:
        lista[0].append(d)
    else:
        lista[1].append(d)

print('*-'*25)
print(f'Os números digitados foram: {lista}')
lista[0].sort()
lista[1].sort()
print(f'Os números organizados são: {lista}')
print(f'Os números pares são: {lista[0]}')
print(f'OOs números ímpares são: {lista[1]}')