def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')


jogador = str(input('Nome do jogador: '))
acertos = str(input('Marcou quantos gols? '))
if acertos.isnumeric():
    acertos = int(acertos)
else:
    acertos = 0
if jogador.strip() == '':
    ficha(gols=acertos)
else:
    ficha(jogador, acertos)
