import moeda

p = float(input('Digite o preço R$'))
t = float(input('Digite a taxa: '))
print(f'A metade do preço R${p} é R${moeda.metade(p)}')
print(f'O dobro do preço R${p} é R${moeda.dobro(p)}')
print(f'Aumentando {t}%, temos R${moeda.aumentar(p, t)}')
