print('='*20)
print('{}'.format('10 TERMOS DE UMA P.A'))
print('='*20)
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
an = a1 + (10 - 1) * r
for c in range(a1, an+1, r):
    print(c, end=' ')
