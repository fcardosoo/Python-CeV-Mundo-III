'''
Faça um programa que tenha uma função chamada
contador(), que receba três parâmetros: inicio,
fim e passo e realize a contagem.
Precisa realizar três contagens através da função criada:

a) De 1 até 10 de 1 em 1
b) de 10 até 0 de 2 em 2
c) Uma contagem personalizada
'''
from time import sleep


def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if p<0:
        p *= -1
    if p==0:
        p = 1

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=False) #O flush habilita o funcionamento do sleep
            sleep(.5)
            cont += p
        print('FIM!')
        print('*'*30)
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=False)
            sleep(.5)
            cont -= p
        print('FIM!')
        print('*' * 30)


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
print('*' * 30)
contador(ini, fim, pas)