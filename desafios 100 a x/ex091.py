from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'Jogador1': randint(1, 6),
             'Jogador2': randint(1, 6),
             'Jogador3': randint(1, 6),
             'Jogador4': randint(1, 6)}
print('{:.^6}'.format('VALORES SORTEADOS'))
ranking = list()
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('{:.^6}'.format('RANKING'))
for i, v in enumerate(ranking):
    print(f'{i+1}° Lugar: {v[0]} com {v[1]}')
    sleep(1)
