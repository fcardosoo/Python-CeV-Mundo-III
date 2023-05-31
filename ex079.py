'''Adicionar valores enquanto o usuário desejar
e adiciona-los em uma lista.
Não acicionar números repetidos;
Mostrar todos os valores digitados em
ordem crescente'''

print('-='*30)

numeros = []

while True:
    n = int(input('Digite um valor: '))

    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não será inserido!')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-='*30)
numeros.sort()
print(f'Você digitou os numeros {numeros}')
print('-='*30)