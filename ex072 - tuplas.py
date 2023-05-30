# criar uma tupla preenchida de ZERO a VINTE
#por extenso. solicitar um número arabico entre
#0 e 20 e mostrar o valor por extenso.

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezeseis',
           'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = -1
    if num <0 or num>20:
        num = int(input('Digite um número de ZERO a VINTE [0 - 20]: '))
        while num<0 or num>20:
            num = int(input('Valor inválido!!!\nDigite um número de ZERO a VINTE [0 - 20]: '))

    print('Você digitou o número ', numeros[num])
    print('~'*20)

    c = str(input('Deseja continuar? ').upper().strip()[0])
    if c == 'N':
        break
print('FIM')
