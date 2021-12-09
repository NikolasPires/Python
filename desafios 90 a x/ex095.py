time = list()
jogador = dict()
dados = list()
s = 0
while True:
    dados.clear()
    s = 0
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    if jogador['partidas'] != 0:
        for g in range(0, jogador['partidas']):
            gols = int(input(f'   Quantos gols na partida {g+1}? '))
            dados.append(gols)
            s += gols
    jogador['gols'] = dados[:]
    jogador['total'] = s
    time.append(jogador.copy())
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for i, e in enumerate(time):
    print(f'{i:>3} ', end='')
    for v in e.values():
        print(f'{str(v):<15}', end='')
    print()
while True:
    perg = int(input('Buscar dados de qual jogador? (999 para parar) '))
    if perg == 999:
        break
    elif perg >= len(time):
        print(f'Erro!! não existe um jogador com o código {perg}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[perg]["nome"].upper()}:')
        for i, e in enumerate(time[perg]['gols']):
            print(f'    No jogo {i+1} ele fez {e} gols')
