'''
função notas() que pode receber várias notas informadas
pelo usuário. Retornar um dicionário com as seguintes informações
- Qnt de notas
- A maior nota
- A menor nota
- A média da turma
- A situação opcional
*** Adicionar também um DOCSTRINGS
'''

def notas(*n, sit=True):
    """
    -> Analisar notas e situções dos alunos
    :param n: uma ou mais notas (aceita várias)
    :param sit: valor opcional
    :return: dicionáro com várias informações sobre a turma
    """
    r = dict()
    r['total'] = len(n)
    r['max'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >=7:
            r['Situação'] = 'BOA'
        elif r['média'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

# Programa principal
resp = notas(5.5, 2.5, 8.5, 1, 5, 9, 1, 5, 0.7, 7.7)
print(resp)
help(notas)