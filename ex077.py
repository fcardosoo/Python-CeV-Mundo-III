'''
criar uma tupla com diversas palavras (não usar acentos)
para cada palabra mostrar suas vogais.
'''

lista = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO',
         'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO',
         'PROGRAMADOR', 'FUTURO')
for p in lista:
    print(f'\nNa palavra {p}, temos: ', end = ' ')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra, end = ' ')