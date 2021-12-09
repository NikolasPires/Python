jogador = dict()
dados = list()
s = 0
jogador['Nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
if jogador['partidas'] != 0:
    for g in range(0, jogador['partidas']):
        gols = int(input(f'   Quantos gols na partida {g}? '))
        dados.append(gols)
        s += gols
jogador['gols'] = dados
jogador['total'] = s
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-='*30)
print(f'O jogador {jogador["Nome"]} jogou {jogador["partidas"]}')
for p, g in enumerate(dados):
    print(f'     => Na partida {p}, fez {g} gols')
