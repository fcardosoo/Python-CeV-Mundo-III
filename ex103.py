"""
Função ficha(), que receberá dois parâmetros opcionais
nome() de um jogador e quantos gols ele marcou
mostrar a ficha do jogador mesmo que algum dado seja informado.
por padrão < jogador=desconhecido> <gols=0>
"""

def ficha(jog="desconhecido", gol=0):
    print(f'O Jogador {jog}, fez {gol} gol(s) no campeonato.')

# Programa principal
nome = str(input("Nome do jogador: "))
gols = str(input("Número de gols: "))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == "":
    ficha(gol=gols)
else:
    ficha(nome, gols)
