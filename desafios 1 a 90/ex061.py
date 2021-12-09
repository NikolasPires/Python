print('GERADOR DE P.A')
print('=#' * 6)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
cont = 0
while cont <= 10:
    print(a1, end=' ')
    a1 += r
    cont += 1
