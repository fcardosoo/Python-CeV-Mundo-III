'''
Faça um programa que tenha uma função
maior(),  que receberá vários parâmetros com
valores inteiros.

Seu programa tem que analisar e dizer qual
deles é o maior.

Usar desempacotamento
'''
from time import sleep

def maior(*num):
    cont = maior = 0
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print()
    sleep(.5)
    print(f'Foram informados {cont} valores ao todo!')
    sleep(.5)
    print(f'O maior valor informado foi {maior}.')
    sleep(.5)


# Programa principal
print('*'*40)
maior(2, 0, 4, 5, 7, 1)
print('*'*40)
maior(4, 7, 0)
print('*'*40)
maior(1, 2)
print('*'*40)
maior(6)
print('*'*40)
maior()