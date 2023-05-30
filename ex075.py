'''
ler quatro valores pelo teclado e armazena-los em uma tupla
Mostrar quantas vezes apareceu o valor 9
em que posição apareceu o primeiro valor 3 (Se não foi digitado informar mensagem na tela)
quais foram os números pares
'''
num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),)

print('~'*40)
print(f'Você digitou os numeros: {num}')
print(f'O número 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('O valor não não digitado em nenhuma posição!')
print(f'Os valores pares digitados foram: ', end=' ')
for n in num:
    if n % 2 ==0:
        print(n, end=' ')