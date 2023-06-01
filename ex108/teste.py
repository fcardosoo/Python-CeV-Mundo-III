import moeda

p = float(input('Digite o preço R$'))
t = float(input('Digite a taxa: '))
print(f'A metade do preço {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro do preço {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando {t:.2f}%, temos {moeda.aumentar(p, t, True)}')
print(f'Reduzindo {t:.2f}% do preço, temos {moeda.diminuir(p, t, True)}')
