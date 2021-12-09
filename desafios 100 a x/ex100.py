from time import sleep
from random import randint
lista = list()


def sorteia():
    print('Sorteando 5 números...')
    for n in range(0, 5):
        ran = randint(0, 9)
        sleep(0.5)
        lista.append(ran)
        print(ran, end=' ')
    print()


def somapar():
    s = 0
    for n in lista:
        if n % 2 == 0:
            s += n
    print(f'Somando os valores pares em {lista}, temos {s}')


sorteia()
somapar()
