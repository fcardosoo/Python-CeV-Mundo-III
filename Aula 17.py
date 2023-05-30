# ***** LISTAS *****

# Abaixo uma TUPLA entre ()
# As tuplas são IMUTÁVEIS
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')

# Abaixo uma LISTA entre []

# As listas podem ser modificadas durante a execução do algorítimo
lanches = ['hamburguer', 'suco', 'pizza', 'pudim']
print('-'*60)
print('mostrando a lista')
print(lanches)

# ADICIONANDO 'cookie' no fim de uma lista
print('-'*60)
print('Adicionando um item ao fim da lista com comando APPEND')
lanches.append('cookie')
print(lanches)

# ADICIONANDO 'cachorro quente' em uma posição específica
print('-'*60)
print('Adicionando um elemento na posição ZERO com o comando INSERT(0,'')')
lanches.insert(0,'cachorro quente')
print(lanches)
print('-'*60)

# REMOVENDO um elemento da lista
# del.nomeDaLista[posição] ex.: del lanches[3] ou
# nomeDaLista.pop(posição) ex.: lanches.pop(3) - *Mais utilizado para eliminar o último elemento
# nomeDaLista.remove(item) ex.: lanches.remove('pizza')

print('Removendo o item 3 "pizza" da lista com o comando del')
del lanches[3]
print(lanches)
print('-'*60)

print('Removendo o último item (cookie) com o comando pop()')
lanches.pop()
print(lanches)
print('-'*60)

print('Removendo o item (suco) com o comando remove(´suco´)')
lanches.remove('suco')
print(lanches)
print('-'*60)

# Para remover um ITEM quando NÃO houver certeza de sua presença
# é possível usar uma estrutura 'if'
# if 'NomeDoItemARemover' in 'nomeDaLista':
#       nomeDaLista.remove('item a remover')

print('Verificando a presença do item PUDIM, se tiver em qualquer posição, então REMOVA')
print(lanches)
print('removendo....')
if 'pudim' in lanches:
    lanches.remove('pudim')
print(lanches)
print('-'*60)

# É Possível CRIAR uma lista com o comando LIST
# valores = list(range(4,11)) - para criar de 4 a 10
print('Criado uma lista com o comando "LIST')
valores = list(range(4,11))
print(valores)
print('-'*60)

# Para ordenar a lista acima usar o comando SORT
print('Criando uma lista fora de ordem')
val = [8,2,5,4,9,3,0]
print(val)
print('Ordenando a lista acima com o comando SORT')
val.sort()
print(val)
print('-'*60)

# Para ordenar INVERSAMENTE use o reverse
print('INVERTENDO a ordem da lista abaixo com o comando "reverse":')
print(val)
val.sort(reverse=True)
print(val)
print('-'*60)

# para contar os valores da lista usar LEN
print('Contar os elementos de uma lista com o "len"')
print(val)
print(f'a lista val possui: {len(val)} elementos')
print('-'*60)
# PRATICANDO
print('Praticando....')
num = (2, 5, 9, 1)
print(f'criando a tupla {num}')
# num[2] = 3 -> Não é possível alterar TUPLAS desta forma

#alterando a TUPLA acima para uma LISTA mudando () para []
print('Alteranco () para [] para converter a TUPLA em LISTA')
numer = [2, 5, 9, 1]
print('Alterando a para lista com o uso de []', numer)
print('-'*60)

#alterando o 9 para 3
print('Alterando o nr 9 para 3')
print(numer)
numer[2] = 3
print(numer)
print('-'*60)

# Adiconando um número
print('Adicionando o número 7 no final com o APPEND')
print(numer)
numer.append(7)
print(numer)
print('-'*60)

print('contando os elementos de uma lista com o "len"')
print(f'Esta lista tem {len(numer)} elementos!')
print('-'*60)
print('Inserindo o valor ZERO com o comando "insert" na posição 2')
numer.insert(2, 0)
print(numer)

print('-'*60)
print('Removendo o último elemento com o comando pop()')
print(numer)
numer.pop()
print(numer)
print('-'*60)

# criando uma nova lista

vamo = []
vamo.append(5)
vamo.append(9)
vamo.append(4)

print('Mostrando os valores formatados')
for v in vamo:
    print(f'{v}...', end = ' ')
print('\n')
print('-'*60)

print('mostrando os indices dos valores')
for c, v in enumerate(vamo):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')
print('\n')
print('-'*60)

''' LER VALORES E INSERIR EM LISTAS'''

dados = []

for cont in range(0, 5):
    dados.append(int(input('Digite um valor: ')))
print(dados)

for c, t in enumerate(dados):
    print(f'Na posição {c} encontrei o valor {t}!')
print('FIM')

print('-'*60)

# Abaixo 'b' recebendo 'a' cria um vínculo entre as listas, uma modificação
# em 'b' também modifica 'a'


a = [2,3,4,7]
b = a

print(f'A lista A: {a}')
print(f'A lista B: {b}')
print('inserindo o comando b[2]=8 para modificar o valor 4 para 8 apenas na lista b')

b[2]=8

print('Mostrando abaixo o resultado do comando nas listas (a) e (b)')
print(a)
print(b)
print('Percebe-se que o valor 4 foi substituido por 8 nas duas listas, mesmo o comando'
      'solicitando mudança apenas na lista (b)')

print('-'*60)

# CRIANDO UMA CÓPIA DE UMA LISTA

print('Para criar uma cópia usar a estrutura   b=a[:]   desta forma a importação'
      'é feita de cada elemento de (a) sem criar o vínculo')

d = [2,4,6,7,7,8,9]
e = d[:]

print(f'Criando a lista\n d: {d}\n'
      f'criando a (e) que recebe todos os elementos de (d)\n'
      f'e: {e}')

print('-'*60)

print('inserindo o comando e[2]=0 para mudar o valor na posição 2 que\n'
      'atualmente é 6 para zero(0)')
e[2]=0

print(e)
print('Lista com o valor na posição 2 alterado')

print('-'*60)