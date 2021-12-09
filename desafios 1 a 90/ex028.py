from random import randint
from time import  sleep
print('-=-'*18)
print('Pensarei em um número de 0 à 5. Tente adivinhar...')
print('-=-'*18)
sleep(1)
num = randint(0, 5)
r = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(2)
if r == num:
    print('Parece que temos um Sherlock Holmes aqui')
else:
    print('Ixe errou... \nParece que lhe faltou curso de adivinha :D \nEu pensei em {} e não em {}'.format(num, r))