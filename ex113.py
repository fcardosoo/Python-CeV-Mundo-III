'''
reescreva a função leiaInt() do desafio 104,
incluindo agora a possibilidade de digitação de um
número de tipo inválido.
Aproveite e crie também uma função
leiaFloat() com a mesma funcionalidade
'''

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! por favor, digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('O usuário interrompeu a entrada de dados!')
            break
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[0;33mERRO! por favor, digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('O usuário interrompeu a entrada de dados!')
            break
        else:
            return n


#programa principal
i = leiaInt('Didigte um número Inteiro: ')
f = leiaFloat('Digite um número Real: ')
print(f'O valor Inteiro digitado foi {i}')
print(f'O valor Real digitado foi {f}')
#r = float(input('Digite um número real: '))