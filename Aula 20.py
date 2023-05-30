# FUNÇÃO está associado a ROTINA
# exemplo:


# Função SEM parâmetro

def mostralinha():
    print('-'*30)


mostralinha()
print('     SISTEMA DE ALUNOS     ')
mostralinha()
mostralinha()
print('     CADASTRO DE FUNCIONÁRIOS     ')
mostralinha()
mostralinha()
print('     ERRO DO SISTEMA     ')
mostralinha()

# -----------------------------------------------
print()
print('*'*50)

#Função COM parâmetro

def mensagem(msg): #dentro dos parenteses está o parâmetro externo
    print('---------------------')
    print(msg) #aqui o parâmetro será exi
    print('---------------------')


mensagem('SISTEMA DE ALUNOS')


print('*'*50)
# -----------------------------------------------
print()

def título(txt):
    print('-'*30)
    print(txt)
    print('-' * 30)


título('     CURSO DE PYTHON     ')
título('     PYTHON É 10!!!     ')
título('     Oi     ')

print('*'*50)
# -----------------------------------------------

#EXEMPLO 1

def soma(a,b):
    s = a+b
    print(s)
    print('-='*15)


#programa principal

soma(4,5)
soma(8,9)
soma(2,1)

print('*'*50)
# -----------------------------------------------

def contador(*núm): # O * desempacota o contador para somar quantos números tiver
    for i in núm:
        print(i, end=' ')
    print('FIM')
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números.')


contador(8, 8)
contador(5, 7, 3, 1, 4)
contador(8, 4, 7)


print('*'*50)
print('outro exemplo de desempacotamento')

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando so valores {valores} temos {s}')

soma(5, 2)
soma(2, 9, 4)

print('*'*50)
print()

# -----------------------------------------------

# Usando listas
# Criar uma função que DOBRA uma Lista

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [7, 2, 5, 0, 4]
print(valores)
dobra(valores)
print(valores)
