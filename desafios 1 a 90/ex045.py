from time import sleep
from random import randint
print('[ 0 ] \033[31mPEDRA\033[m')
print('[ 1 ] \033[32mPAPEL\033[m')
print('[ 2 ] \033[33mTESOURA\033[m')
lista = ['PEDRA', 'PAPEL', 'TESOURA']
choic = int(input('Qual é a sua escolha? '))
sleep(1)
print('\033[35mJO')
sleep(1.5)
print('KEN')
sleep(2)
print('PO!!!\033[m')
computer = randint(0, 2)
if computer == 1 and choic == 2 or computer == 2 and choic == 0 or computer == 0 and choic == 1:
    condition = '\033[34mVITÓRIA'
elif computer == 2 and choic == 1 or computer == 0 and choic == 2 or computer == 1 and choic == 0:
    condition = '\033[31mDERROTA'
else:
    condition = '\033[37mEMPATE'
print('=' * 24)
print('Computador jogou {}'.format(lista[computer]))
print('Jogador jogou {}'.format(lista[choic]))
print('='*24)
print(condition)
