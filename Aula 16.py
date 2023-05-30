'''   TUPLAS
As tuplas se apresentam entre ()
As listas se apresentam entre []
Os dicionarios se apresentam entre {}
'''

lanche = ('hamburguer', 'suco', 'pizza', 'pudim') #A partir da versão 3.5 não é necessário utilizar () nas tuplas
print(lanche)

print('~'*15)
print(lanche[1]) #é o suco, já que o hambúrguer é o ZERO
print('~'*15)
print(lanche[3]) # é o último 'pudim'
print('~'*15)
print(lanche[-2]) #conta do fim para o início (o último ítem é o -1)
print('~'*15)
print(lanche[1:3]) # Fatiamento - Mostra do item 1 até o 2 - o item 3 é exclcuído.
print('~'*15)
print(lanche[2:]) #Assim mostra do elem 2 até o final
print('~'*15)
print(lanche[:2]) #Assim mostra do início ate o 1 o 2 é excluído
print('~'*15)
print(lanche[-2:]) #Mostra começando no -2 (pizza) até o final (pudim)
print('~'*15)
print(lanche[-3:]) #Começa no -3 (suco) até o final
print('~'*15)
print(lanche) #mostra toda a tupla
print('~'*15)

#TUPLAS SÃO IMUTÁVEIS
#Abaixo tentativa de mudar uma tupla
#O Python retornará erro
# lanche[1] = 'Refrigerante'

#Usando um for em uma tupla

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
print('~'*15)

#Exibir a quant itens na tupla
print('A tupla possui: ', len(lanche), 'itens')

print('~'*15)

# Adicionando um item a tupla
# Modifiquei o nome para 'laches'

lanches = ('hamburguer', 'suco', 'pizza', 'pudim', 'Batata Frita')

# Outra maneira de usar o for:
# Lembrando que no range ele ignora o último elemento... indo de 0 a 4

for cont in range(0, len(lanches)):
    print(cont)
print('~'*15)
# Para mostrar os nomes dos lanches é necessário incluir
#uma pequena modificação no print
for cont in range(0, len(lanches)):
    print(lanches[cont])
print('~'*15)
#Usando um print formatado
for cont in range(0, len(lanches)):
    print(f'Eu vou comer {lanches[cont]}')

print('~'*15)

# Mostrando a posição:
for cont in range(0, len(lanches)):
    print(f'Eu vou comer {lanches[cont]} na posição {cont}')
print('~'*15)

# Mostrando a posição sem usar o range:
for pos, comida in enumerate(lanches):
    print(f'Eu vou comer {comida} na posição {pos}')
print('~'*15)

#SE NÃO PRECISAR DA POSIÇÃO:
for comida in lanches:
    print(f'Eu vou comer {comida}!')
print('~'*15)
# Mostrar em ordem Alfabetica

print(sorted(lanches))
print('~'*15)

# Unindo TUPLAS *A ordem importa a+b dif b+a
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b

print(a)
print(b)
print(c)
print('~'*15)

print(len(c))

#Para saber quantas vezes um elemento (5) se repete dentro de C
print(c.count(5))

# Para saber a posição de um elemento na tupla usar 'index'
print(c.index(8)) #na posição 4

print('~'*15)

# Usando a propriedade INDEX do objeto tupla
#este comando retorna a posição do numero 8
print(c)
print(c.index(8))

print('~'*15)
# Temos 2 numeros 2 na lista um na posição ZERO e outro na posição
# SEIS, para mostrar a posição do segundo seis indicamos que a busca
# deve começar a partir da posição 1 (x, 1)
print(c)
print(c.index(2, 1))

print('~'*15)

# As tuplas no PYTHON pode aceitar letras e números:

pessoa = 'Fabiano', 41, 'M', 99.88
print(pessoa)

# Para apagar uma tupla usar del(nome da tupla)

del(pessoa) # apagando a tupla pessoa
#print(pessoa) - este comando daá erro pois apagamos a tupla pessoa anteriormente
