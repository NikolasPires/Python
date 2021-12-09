brasileirao = ('Palmeiras', 'Atlético - MG','Bragantino', 'Fortaleza',
               'Flamengo','Athletico - PR', 'Ceará', 'Santos', 'Atlético - GO',
               'Bahia', 'Corinthians', 'Fluminense', 'Juventude', 'Sport',
               'Internacional', 'Cuiabá','São Paulo', 'América - MG',
               'Grêmio', 'Chapecoense')
print(f'Os cinco primeiro times são: {brasileirao[0:5]}')
print(f'Os últimos 4 colocado são: {brasileirao[-4:]}')
print(f'Os times em ordem alfabética são:'
      f'{sorted(brasileirao)}')
print(f'Chapecoense está na posição {brasileirao.index("Chapecoense") + 1}º')