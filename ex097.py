''' Faça um programa que tenha a função
escreva(), que receba um texto qualquer
como parâmetro e mostre uma mensagem
com tamanho adaptável

Ex.:

~~~~~~~
Fabiano
~~~~~~~

~~~~~~~~~~~
Hello World
~~~~~~~~~~~
'''

def escreva(a):
    for i in a:
        print('~',end='')
    print()
    print(a)
    for i in a:
        print('~',end='')


# Programa principal

print('--- Controle de Margens ---')
palavra = input('Digite uma palavra: ')
escreva(palavra)

# Solução do Guanabara
print()


def escr(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# main
escr(input('Digite uma mensagem: '))