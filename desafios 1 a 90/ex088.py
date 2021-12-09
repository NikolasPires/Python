from random import randint
from time import sleep
tot = 1
mega = list()
dados = list()
print('-'*30)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('-'*30)
jogos = int(input('Quantos jogos você quer que eu jogue? '))
while tot <= jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in mega:
            dados.append(num)
            cont += 1
        if cont >= 6:
            break
    dados.sort()
    mega.append(dados[:])
    dados.clear()
    tot += 1
print('-='*3, f' SORTEANDO {jogos} JOGOS ', '=-'*3)
for i, l in enumerate(mega):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
