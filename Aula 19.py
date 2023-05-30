# DICIONÁRIOS

dados = {} # criando um dicionário
dados1 = dict() # Outra forma de criar dicionários

print(f'Mostrando o dicionário criado: {dados}')
dados['nome'] = 'Pedro'

print(f'Mostrando após inserir o elemento nome: {dados}')

dados['idade'] = 25
print(f'Mostrando após inserir idade: {dados}')

dados['sexo'] = 'M'
print(f'Mostrando após inserir sexo: {dados}')

# Apagando um elemento do dicionário

del dados['idade']
print(f'Mostrando após apagar idade: {dados}')

# Criando a biblioteca FILMES
# Esta estrutura possui ITENS, CHAVES e VALORES
print('-='*30)
filme = {'titulo':'Star Wars',
         'ano': 1977,
         'diretor':'George Lucas'
         }
print(filme.values()) #Método interno que retorna VALORES
print(filme.keys()) #Mostrando as CHAVES
print(filme.items()) #Mostra os ITENS (chaves e valores)

print('='*60)

# Utilizando os conceitos acima para LAÇOS

for k,v in filme.items():
    print(f'O {k} é {v}')

print('-='*30)


# Colocando um DICIONÁRIO dentro de uma LISTA

locadora =[]

locadora.append(filme)
print(locadora)

filme1 = {'titulo': 'Avengers',
          'ano': 2012,
          'diretor': 'Joss Whedon'}
filme2 = {'titulo': 'Matrix',
          'ano': 1999,
          'diretor': 'Wachowski'}

locadora.append(filme1)
print(locadora)
locadora.append(filme2)
print(locadora)

print('*'*60)

print('Buscando valores em um dicionário...')
print(f'O ano do primeiro filme {locadora[0]["titulo"]} é: ',locadora[0]['ano'])

print('-='*30)

pessoas = {'nome': 'Ana',
           'sexo': 'F',
           'idade': 28}

print(pessoas)

#Alterando o nome da chave
print()
print('Alterando o Nome "Ana" para "Laura".')
print()
pessoas['nome'] = 'Laura'
print(pessoas)
print()
print('Adicionando o elemento peso')

pessoas['peso'] = 51.5
print(pessoas)
print('-='*30)

# Colocar um dicionário dentro de uma lista
print('Criando um dicionário dentro de uma LISTA')
print()

brasil = []
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo','sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil[0])

print('-='*30)
print()

estados = dict()
brasil = list()

for c in range(0, 3): #Usar o 'for' para digitar 3 estados
    estados['UF'] = str(input('Unidade Federativa: '))
    estados['Sigla'] = str(input('Sigla do estado: '))
    brasil.append(estados.copy()) #Usar o copy() para adicionar elementos do dicionário em uma lista
print(brasil)
print('~~'*30)
print()

for e in brasil: # Mostrar os itens criados
    # print(e) # mostra a UF e a Sigla
    for k, v in e.items():
        print(f'O campo {k} tem o valor {v}')

print('-='*30)
print()
print('Outra forma de exibição...')

for e in brasil:
    for v in e.values(): #Mostra os valores sem as chaves
        print(v, end=' ') # usar o end para mostrar os valores lado a lado
    print()

print('-='*30)
print()

