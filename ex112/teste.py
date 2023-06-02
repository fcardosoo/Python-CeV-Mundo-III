from ex112.utilidades import moeda
from ex112.utilidades import dado

p = dado.leiaDinheiro('Digite o preço R$')
ta = float(input('Digite a taxa de aumento: '))
tr = float(input('Digite a taxa de redução: '))
moeda.resumo(p, ta, tr)
