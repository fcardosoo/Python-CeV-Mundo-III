''' Criar lista com varios números de acordo
com o usuário. Mostrar:
a) Quantos numeros foram digitados
b) Lista de valores decrescente
c) Se o valor 5 foi digitado'''

lista = []

while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    cont = str(input('Deseja continuar? [S/N] '))
    if cont in 'Nn':
        break
print('-*-'*20)
print(f'Você digitou {len(lista)} números!')
print(f'A lista foi digitada na ordem {lista}')
print(f'Em ordem decrescente fica... ', end = ' ')
lista.sort(reverse=True)
print(lista)

if 5 in lista:
    print('Você diditou o Número 5!')
else:
    print('Você não digitou o número 5!')