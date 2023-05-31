'''Ler vários numeros e colocar em uma lista
A partir disso criar duas listas separando
os numeros pares dos ímpares.
Mostrar as 3 listas'''

num = []
par = []
impar = []

while True:
    n = int(input('Digite um número: '))
    num.append(n)
    if n%2 == 0:
        par.append(n)
    else:
        impar.append(n)
    cont = str(input('Deseja continuar? [S/N] '))
    if cont in 'Nn':
        break
print('-*'*30)
print(f'Você digitou os valores: {num}')
print(f'Os valores pares correspondem aos: {par}')
print(f'Enquanto que os ímpares são: {impar}')