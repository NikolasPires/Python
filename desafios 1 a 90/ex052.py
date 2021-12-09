cont = 0
lista = ['1', '2', '3']
np = int(input('Digite um número: '))
for c in range(1, np + 1):
    if np % c == 0:
        cont += 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(np, cont))
if cont > 2:
    print('Portanto ele NÃO É PRIMO')
else:
    print('Ele foi divisível 2 vezes logo é PRIMO')
