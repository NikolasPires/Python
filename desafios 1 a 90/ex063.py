print('=' * 11)
print('{}'.format('RAZÃO AUREA'))
print('=' * 11)
termos = int(input('Digite o números de termos da razão aurea: '))
cont = 3
t1 = 0
t2 = 1
print('{} {}'.format(t1, t2), end='')
while cont <= termos:
    cont += 1
    t3 = t1 + t2
    print(' {}'.format(t3), end='')
    t1 = t2
    t2 = t3
print(' FIM')
print('=' * 11)