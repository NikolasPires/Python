print('GERADOR DE P.A')
print('=#' * 6)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
cont = 0
n = 0
ocont = 1
while cont <= 10:
    print(a1, end=' ')
    a1 += r
    cont += 1
    if cont == 10:
        n = int(input('\nQuantos termos você quer mostrar a mais? '))
        if n > 0:
            while ocont != n:
                ocont += 1
                print('{}'.format(a1), end=' ')
                a1 += r
        elif n == 0:
            print('FIM')
print('\nHouveram {} termos no total'.format(cont + (ocont - 1)))
'''print('GERADOR DE P.A')
print('=#' * 6)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
cont = 1
total = 0
n = 10
while n != 0:
    total += n
    while cont <= total:
        print(a1, end=' ')
        a1 += r
        cont += 1
    print('PAUSA')
    n = int(input('Quantos termos a mais? '))
print('\nHouveram {} termos no total'.format(total))'''