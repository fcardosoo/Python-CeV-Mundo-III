"""
função 'fatorial' que receberá 2 parâmetros
numero() e show() que indicará se será mostrado o
cálculo na tela
"""

def fatorial(numero, show = False):
    """
    -> Calcula o Fatorial de um número.
    :param numero: O número a ser calculado
    :param show: (opcional) Mostra aou não a conta
    :return: O valor fatorial de um número.
    """
    num = 1
    fat = 1
    if numero>num:
        num = numero
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fat *= c
    return fat


#Programa principal
print('~~~~ FATORIAL ~~~~')
print(fatorial(5, show=True))
help(fatorial)