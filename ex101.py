"""
crie uma função chamada 'voto()'
recebe como parâmetro 'ano de nascimento' retornando um valor
'literal' indicando se uma pessoa tem voto NEGADO, OPCIONAL ou
OBRIGATÓRIO.
"""

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
    elif idade <18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


print('*'*30)
print('~~~~~~ Analise de idade ~~~~~~')

print(voto(int(input('Digite seu ano de nascimento: '))))
print('*' * 30)