# Funções parte 2

# INTERACTIVE HELP
# USAR A FUNÇÃO 'help()'

# help()


# DOCSTRINGS -> Criar um manual para a função criada

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: Inicio da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: Sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print("FIM!")


contador(0, 10, 2)

help(contador)

print('*' * 50)
print('Parâmetro opcional!!!')


def somar(a=0, b=0, c=0): #declarar o valor como =0 permite que sejam informados menos de 3 parâmetros... inclusive nenhum
    """
    Função para somar até 3 valores
    :param a: valor 1
    :param b: valor 2
    :param c: valor 3
    :return: sem retorno
    """
    s = a + b + c
    print(f'A soma é {s}')


somar()
somar(1)
somar(1, 2)
somar(1, 2, 3)

print('*' * 50)

# ESCOPO DE VARIÁVEIS

# RETORNO DE VALORES

# Para usar o retorno de valores precisamos ter uma variável de resposta
# para receber o retorno

def somar (a=0,b=0,c=0):
    s=a+b+c
    return s


r1 = somar(3,2,5)
r2 = somar(1,8)
r3 = somar(3,12,5)

print(f'As somas valem {r1}, {r2} e {r3}')

print('*' * 50)
print('EXERCÍCIO PRÁTICO')

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

print('*' * 50)
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')

print('*' * 50)

def par(n=0):
    if n%2 ==0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
print(par(num))

if par(num):
    print(f'O valor {num} é par!')
else:
    print(f'O valor {num} é ímpar!')
