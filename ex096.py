''' Faça um programa que tenha uma
função chamada área(), que receba
as dimensões de um terreno retangular
(l x c) e mostre a área do terreno;
'''


def area(l, c):
    a = l * c
    print(f'A propriedade tem {c}m por {l}m e área de {a}m²')


#Programa Principal:
a = float(input('Informe o comprimento: '))
b = float(input('Informe a largura: '))
area(a, b)
